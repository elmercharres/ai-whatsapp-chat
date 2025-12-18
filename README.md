# AI WhatsApp Chat

A FastAPI-based application for managing WhatsApp conversations with AI integration for order processing and customer service.

## Features

- Multi-tenant support
- WhatsApp integration via Twilio
- AI-powered chat responses
- Product and order management
- PostgreSQL database with SQLAlchemy ORM

## Project Structure

```
ai-whatsapp-chat/
│
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration management
│   ├── database.py             # Database connection setup
│   ├── logging_conf.py         # Logging configuration
│   │
│   ├── models/                 # SQLAlchemy models
│   │   ├── tenant.py
│   │   ├── product.py
│   │   └── order.py
│   │
│   ├── repositories/           # Data access layer
│   │   ├── tenant_repo.py
│   │   ├── product_repo.py
│   │   └── order_repo.py
│   │
│   ├── services/               # Business logic layer
│   │   ├── whatsapp_service.py
│   │   ├── ai_service.py
│   │   ├── prompt_builder.py
│   │   └── order_service.py
│   │
│   └── api/                    # API endpoints
│       └── whatsapp.py
│
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Setup

1. **Clone the repository**
   ```bash
   cd ai-whatsapp-chat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Edit `.env` file with your credentials:
   - Database URL
   - Twilio credentials
   - AI API key

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `TWILIO_ACCOUNT_SID`: Twilio account SID
- `TWILIO_AUTH_TOKEN`: Twilio auth token
- `TWILIO_WHATSAPP_NUMBER`: Your Twilio WhatsApp number
- `AI_API_KEY`: API key for AI service (OpenAI, etc.)
- `AI_MODEL`: AI model to use (e.g., gpt-4)
- `APP_ENV`: Application environment (development/production)
- `DEBUG`: Debug mode (True/False)
- `LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING, ERROR)

## API Endpoints

- `POST /webhook/whatsapp` - Receive WhatsApp messages from Twilio
- Additional endpoints as needed

## License

MIT
