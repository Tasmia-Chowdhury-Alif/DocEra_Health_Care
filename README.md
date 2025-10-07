<div align="center">
<img src="https://docera-health-care.vercel.app/static/images/docera_logo.png" alt="DocEra Logo" width="120" height="120">

# DocEra Health Care API

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-5.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/) [![DRF](https://img.shields.io/badge/DRF-REST-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
<br>
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![Stripe](https://img.shields.io/badge/Stripe-008CDD?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com/) 
<br>
[![Vercel](https://img.shields.io/badge/Deployed-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)
[![License](https://img.shields.io/badge/License-MIT-FFA500?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

</div>

---

## ⚡ Overview  

**DocEra Health Care** is a **secure and scalable hospital management API** built with **Django & Django REST Framework**.  
It handles **authentication, appointments, payments, doctors, patients, reviews, and services** with strong emphasis on **security, scalability, and clean architecture**.  

👉 **Frontend** integration coming soon!  

**🚀 Live API:** [docera-health-care.vercel.app](https://docera-health-care.vercel.app/)  
**📚 Swagger Docs:** [Swagger UI](https://docera-health-care.vercel.app/api/swagger/)  
**🎯 Redoc Docs:** [Redoc](https://docera-health-care.vercel.app/api/redoc/)  
**Custom Admin Panel (Demo for Doctors):** [Admin UI](https://docera-health-care.vercel.app/admin/)  
   - 👨‍⚕️ Username: `jashim`  
   - 🔑 Password: `DocEraDemo123`  

---

## ✨ Features  

 ### 🔐 **Authentication & Roles**  
  - JWT-based login with email verification.  
  - Auto-role assignment: Patients (default), Doctors (admin-assigned).  

 ### 👨‍⚕️ **Doctors**  
  - Profiles with bio, specialization, designations, availability, and fees.  
  - Reviews & ratings system ⭐⭐⭐⭐⭐.  

 ### 🧑‍💼 **Patients**  
  - Profiles auto-created on signup.  
  - Data isolation: users see only their own info.  

 ### 📅 **Appointments**  
  - Online (Stripe payments + webhook verification + email notifications).  
  - Offline appointments with email notifications.  
  - Smart cancellation (within 24h and refund for online appointments).  

 ### 💳 **Payments**  
  - Secure Stripe integration with refund handling.  

 ### 📧 **Emails**  
  - Account activation, password reset, booking confirmations.  

 ### 🏥 **Hospital Services & Contact**  
  - CRUD for services.  
  - Public inquiry/contact forms.  

 ### 📖 **API Documentation**  
  - **API Versioning:** URLPathVersioning → `/api/v1/`.  
  - **Enhanced OpenAPI Schema:** Custom tags, enums, request/response examples via **drf-spectacular**.  
  - **Interactive Docs:** Swagger UI + Redoc.  

 ### 🔧 **Developer Experience**  
  - Integrated **Django Debug Toolbar** for monitoring & debugging.  
  - Refactored views/serializers with inline docs for maintainability.  


---

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2+ (Core application framework)
- **API Framework**: Django REST Framework (RESTful API development)
- **Authentication**: Djoser + SimpleJWT (JWT-based auth management)
- **Database**: PostgreSQL (Production data storage)
- **Payment Processing**: Stripe (Secure payment handling)
- **API Documentation**: drf-spectacular (OpenAPI schema generation)
- **Admin Interface**: Jazzmin + CKEditor5 (Enhanced admin experience)
- **Deployment**: Vercel (Cloud hosting platform)
- **Development Tools**: Django Debug Toolbar (Performance monitoring)

---

## ⚙️ Quick Setup Guide
To run locally (requires Python 3.12+):

1️⃣ Clone the repository:  
```bash
git clone https://github.com/Tasmia-Chowdhury-Alif/DocEra_Health_Care.git
cd DocEra-Health-Care
```

2️⃣ Create & activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3️⃣ Install dependencies:
```bash
pip install -r requirements.txt

```

4️⃣ Configure Environment Variables (.env):
```env
SECRET_KEY=your_django_secret_key
DJANGO_DEBUG=True
DATABASE_ENGINE=postgresql
DATABASE_URL=your_postgres_url
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
STRIPE_PUBLISHABLE_KEY=your_key
STRIPE_SECRET_KEY=your_key
STRIPE_WEBHOOK_SECRET=your_key
```

5️⃣ Run Migrations & Start Server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

🎉 **Success!** Visit [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/swagger/) to explore the API.

--- 

## 🔮 Coming Soon

 - 🌐 React Frontend integration.
 
 - 🤖 **AI-Powered Recommendations**: Smart doctor matching
  
 - 📋 **Chat System**: Real-time doctor-patient messaging
  
 - 📊 Analytics Dashboard for admins.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Tasmia Chowdhury Alif**

- GitHub: [@Tasmia-Chowdhury-Alif](https://github.com/Tasmia-Chowdhury-Alif)
- Email: tasmiachowdhuryalif222@gmail.com


---

<div align="center">

### ⭐ If this project helped you, please give it a star!

**Built with ❤️ by Tasmia Chowdhury Alif**

[Report Bug](https://github.com/Tasmia-Chowdhury-Alif/DocEra_Health_Care/issues) • [Request Feature](https://github.com/Tasmia-Chowdhury-Alif/DocEra_Health_Care/issues)

</div>
