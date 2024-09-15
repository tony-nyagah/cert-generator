from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from weasyprint import HTML
from .forms import CertificateGenerationForm
from .models import GeneratedCertificate
import tempfile


def generate_certificate(request: HttpRequest):
    if request.method == "POST":
        form = CertificateGenerationForm(request.POST)
        if form.is_valid():
            template = form.cleaned_data["template"]
            participant_name = form.cleaned_data["participant_name"]

            # Render the certificate HTML
            html_string = render_to_string(
                "certificates/certificate_template.html",
                {
                    "participant_name": participant_name,
                    "template": template,
                },
            )

            # Generate PDF
            html = HTML(string=html_string)
            result = html.write_pdf()

            # Save the generated certificate
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".pdf"
            ) as output_file:
                output_file.write(result)
                output_file.flush()

                generated_certificate = GeneratedCertificate(
                    template=template, participant_name=participant_name
                )
                generated_certificate.pdf_file.save(
                    f"certificate_{participant_name}.pdf", output_file
                )

            # Serve the PDF
            response = HttpResponse(result, content_type="application/pdf")
            response["Content-Disposition"] = (
                f'attachment; filename="certificate_{participant_name}.pdf"'
            )
            return response
    else:
        form = CertificateGenerationForm()

    return render(request, "certificates/index.html", {"form": form})
