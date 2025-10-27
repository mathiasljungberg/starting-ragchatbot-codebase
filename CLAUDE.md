# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

**Install dependencies:**
```bash
uv sync
```

**Start the application:**
```bash
./run.sh
```
or manually:
```bash
cd backend && uv run uvicorn app:app --reload --port 8000
```

**Environment setup:**
Create `.env` file in root directory:
```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Architecture Overview

This is a full-stack RAG (Retrieval-Augmented Generation) system for course materials with the following key components:

### Backend (Python/FastAPI)
- **app.py**: Main FastAPI application with CORS, API endpoints (/api/query, /api/courses)
- **rag_system.py**: Core orchestrator connecting all RAG components
- **vector_store.py**: ChromaDB integration with semantic search capabilities
- **ai_generator.py**: Anthropic Claude API integration with tool support
- **document_processor.py**: Processes course documents into chunks
- **search_tools.py**: Tool-based search system for AI agent
- **session_manager.py**: Manages conversation history
- **models.py**: Data models for Course, Lesson, CourseChunk
- **config.py**: Configuration using environment variables

### Frontend (HTML/CSS/JavaScript)
- **index.html**: Single-page chat interface
- **script.js**: Client-side logic for chat functionality
- **style.css**: UI styling

### Key Dependencies
- **chromadb**: Vector database for embeddings storage
- **anthropic**: Claude API client
- **sentence-transformers**: Text embedding models
- **fastapi/uvicorn**: Web framework and server
- **python-dotenv**: Environment variable management

### Data Flow
1. Course documents (PDF/DOCX/TXT) in `/docs` folder are processed into chunks
2. Chunks stored in ChromaDB with embeddings for semantic search
3. User queries trigger tool-based search via Claude
4. Results combined with conversation history for contextualized responses

### Application Structure
- Backend serves API at port 8000
- Static frontend files served from `/frontend` directory
- Course documents loaded from `/docs` directory on startup
- ChromaDB persisted in `./chroma_db` directory

### Configuration
All settings centralized in `config.py` with defaults:
- Chunk size: 800 characters
- Overlap: 100 characters
- Max search results: 5
- Embedding model: "all-MiniLM-L6-v2"
- Claude model: "claude-sonnet-4-20250514"