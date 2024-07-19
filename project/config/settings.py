from pathlib import Path

from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent

settings.configure(
    DEBUG=True,
    SECRET_KEY="your_secrete_here",
    ROOT_URLCONF="project.api.urls",
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ],
    TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
)
