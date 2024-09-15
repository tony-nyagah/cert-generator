from django.db import models


class CertificateTemplate(models.Model):
    name = models.CharField(max_length=100)
    html_template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GeneratedCertificate(models.Model):
    template = models.ForeignKey(CertificateTemplate, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200)
    generated_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to="generated_certificates/")

    def __str__(self):
        return f"Certificate for {self.participant_name}"
