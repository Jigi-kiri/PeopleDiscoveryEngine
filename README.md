# AIFindr - AI-Powered Profile Matching Platform 🤖

AIFindr is an innovative platform that uses AI to match people based on their interests, goals, and vibes. Using natural language processing and semantic search, it helps users find like-minded individuals through intuitive, conversational queries.

## 🌟 Features

- **Natural Language Search**: Simply describe what you're looking for in plain English
- **AI Query Parsing**: Automatically extracts interests and vibes from queries
- **Semantic Matching**: Uses advanced embeddings to find similar profiles
- **Real-time Results**: Instant profile matches with explanations
- **Dark/Light Theme**: Elegant UI with theme switching capability
- **Responsive Design**: Works seamlessly on all devices

## 🛠️ Technology Stack

### Backend
- FastAPI (Python web framework)
- Sentence Transformers (for semantic embeddings)
- FAISS (for efficient similarity search)
- Mistral AI (for natural language processing)
- Uvicorn (ASGI server)

### Frontend
- React (with Vite)
- Modern CSS (with CSS Variables)
- Responsive Design
- Theme Switching
- Interactive UI Components

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Mistral API key

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the backend directory:
```env
MISTRAL_API_KEY=your_api_key_here
MISTRAL_MODEL=mistral-large-latest
```

5. Run the backend server:
```bash
uvicorn main:app --reload
```
Backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
Create a `.env` file in the frontend directory:
```env
VITE_API_URL=http://localhost:8000
```

4. Run the development server:
```bash
npm run dev
```
Frontend will be available at `http://localhost:5173`

## 🔍 Usage

1. Start both backend and frontend servers
2. Visit the frontend URL in your browser
3. Use the search bar with natural language queries like:
   - "Find me artists who love hiking and talk like Tarantino"
   - "Looking for tech enthusiasts with a philosophical bent"
   - "Show me creative people interested in AI and ethics"
4. View matched profiles with their interests and vibes
5. Toggle between light and dark themes using the theme switch

## 🌐 Deployment

The application is configured for deployment on Vercel:

### Backend Deployment
```bash
cd backend
vercel
```

### Frontend Deployment
```bash
cd frontend
vercel
```

Make sure to set up the following environment variables in Vercel:
- Backend: MISTRAL_API_KEY, MISTRAL_MODEL
- Frontend: VITE_API_URL (pointing to your deployed backend URL)

## 🎨 Theme Customization

The application supports full theme customization through CSS variables in `App.css`:
- Light theme colors and styling
- Dark theme colors and styling
- Card layouts and animations
- Typography and spacing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Mistral AI for natural language processing
- Sentence Transformers for semantic embeddings
- FAISS for vector similarity search
- The FastAPI and React communities