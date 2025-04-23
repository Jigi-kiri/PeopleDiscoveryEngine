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

The application is configured for deployment on Render:

### Backend Deployment
1. Create a Render account at [https://render.com/](https://render.com/)
2. Create a `render.yaml` file in the root of your backend directory.
3. Connect your Git repository to Render.
4. Configure your web service:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
5. Set environment variables:
   - `MISTRAL_API_KEY`: Your Mistral API key
   - `MISTRAL_MODEL`: `mistral-large-latest`

### Frontend Deployment
1. Deploy the frontend to Render or Vercel, ensuring the `VITE_API_URL` points to your deployed backend URL.

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

## 💡 Problem-Solving Approach

This section outlines the step-by-step approach taken to develop and deploy the AIFindr application, highlighting the challenges encountered and the solutions implemented.

### 1. Initial Setup and FastAPI Backend

- **Objective**: Set up a basic FastAPI backend with a search endpoint.
- **Steps**:
    - Created `main.py` with a `/search` endpoint.
    - Implemented basic query parsing, embedding generation, and similarity search.
- **Challenges**:
    - Encountered import errors due to relative imports.
    - Faced issues with the structure of the FastAPI endpoint.
- **Solutions**:
    - Switched to absolute imports for better module resolution.
    - Defined the request body using Pydantic models for proper data validation.

### 2. Integrating AI and Semantic Search

- **Objective**: Integrate AI for natural language query parsing and semantic search.
- **Steps**:
    - Used Mistral AI for parsing natural language queries into structured filters.
    - Implemented sentence embeddings using `sentence-transformers` for semantic similarity.
    - Used FAISS for efficient similarity search.
- **Challenges**:
    - Faced issues with the Mistral API key and authentication.
    - Encountered dimension mismatch errors between query embeddings and profile embeddings.
- **Solutions**:
    - Implemented a keyword-based query parser as a fallback when the Mistral API was unavailable.
    - Ensured consistent embedding dimensions by generating embeddings for all profiles using `sentence-transformers`.

### 3. Building the React Frontend

- **Objective**: Create a React frontend for user interaction and displaying search results.
- **Steps**:
    - Set up a basic React application using Vite.
    - Created components for the search bar, profile cards, and theme toggle.
    - Implemented API calls to the FastAPI backend.
- **Challenges**:
    - Encountered difficulties in styling the components and handling asynchronous API calls.
- **Solutions**:
    - Cleaned up the Vite template and removed unnecessary files.
    - Used CSS variables for theme customization and responsive design.
    - Implemented proper error handling and loading states for API calls.

### 4. Theme Customization and UI Enhancements

- **Objective**: Enhance the UI with a dark/light theme toggle and attractive color combinations.
- **Steps**:
    - Implemented a theme toggle using React state and local storage.
    - Defined CSS variables for theme-specific styles.
    - Added hover effects and transitions for a better user experience.
- **Challenges**:
    - Ensuring high contrast and readability in both themes.
    - Creating visually appealing and consistent styling across themes.
- **Solutions**:
    - Used a carefully selected color palette for both light and dark themes.
    - Added borders to cards in dark mode for better visual separation.
    - Improved typography with custom font families and letter spacing.

### 5. Deployment to Render

- **Objective**: Deploy the backend and frontend to a production environment.
- **Steps**:
    - Configured the backend for deployment on Render using a `render.yaml` file.
    - Added a health check endpoint to the FastAPI application for Render's health checks.
    - Updated the frontend to use the deployed backend URL.
- **Challenges**:
    - Initial deployment attempts on Vercel failed due to file size limits and dependency installation problems.
    - Encountered issues with setting up the Render environment and configuring environment variables.
- **Solutions**:
    - Switched to deploying the backend on Render due to persistent issues with Vercel.
    - Created a `render.yaml` file to specify the necessary configuration for Render deployment.
    - Ensured that all environment variables were set correctly in Render.

### 6. Addressing Deployment Issues

- **Objective**: Resolve deployment issues related to file sizes and dependency installation.
- **Steps**:
    - Created `.vercelignore` files to exclude unnecessary files.
    - Used the `--archive=tgz` flag to reduce deployment size.
    - Specified compatible package versions in `requirements.txt`.
    - Configured the `vercel.json` file with the correct Python runtime and install commands.
- **Challenges**:
    - File size limits on Vercel.
    - Dependency installation failures due to incompatible package versions.
- **Solutions**:
    - Switched to deploying the backend on Render due to persistent issues with Vercel.
    - Created a `render.yaml` file to specify the necessary configuration for Render deployment.
    - Ensured that all environment variables were set correctly in Render.

This iterative approach, involving continuous testing, debugging, and refactoring, ensured the successful development and deployment of the AIFindr application.

## 🙏 Acknowledgments

- Mistral AI for natural language processing
- Sentence Transformers for semantic embeddings
- FAISS for vector similarity search
- The FastAPI and React communities