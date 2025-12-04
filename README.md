# AI Agent Code Polisher

An AI-powered code refactoring tool that automatically improves code quality across entire codebases. This tool uses Google's Gemini API to analyze and rewrite code, making it more maintainable, idiomatic, and production-ready while preserving original behavior.

## Features

- **Multi-language Support**: Processes Python, JavaScript, TypeScript, React (JSX/TSX), Java, Kotlin, and Swift
- **Automatic Refactoring**: Improves code clarity, maintainability, and follows language-specific best practices
- **Behavior Preservation**: Ensures refactored code maintains the same external behavior and API compatibility
- **Batch Processing**: Processes entire directories of source files automatically
- **Smart Filtering**: Automatically skips `.git`, `__pycache__`, and `node_modules` directories

## Requirements

- Python 3.5+
- Google API Key for Gemini API

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-agent-code-polisher
```

2. Install required packages:
```bash
pip install openai python-dotenv
```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Project Structure

```
ai-agent-code-polisher/
├── app.ipynb                 # Main Jupyter notebook with the refactoring logic
├── unoptimized-code/         # Input directory: place your code files here
│   ├── sample_one.py
│   └── sample_two.js
└── polished-code/            # Output directory: refactored code appears here
    ├── sample_one.py
    └── sample_two.js
```

## Usage

1. Place your code files in the `unoptimized-code/` directory

2. Open `app.ipynb` in Jupyter Notebook or JupyterLab

3. Update the paths in the notebook if needed:
   ```python
   repo_root = Path("/path/to/your/unoptimized-code")
   output_root = Path("/path/to/your/polished-code")
   ```

4. Run all cells in the notebook. The tool will:
   - Find all supported source files
   - Process each file through the Gemini API
   - Save refactored versions to the output directory

## What Gets Improved

The AI agent focuses on:

- **Code Clarity**: Better naming, structure, and organization
- **Maintainability**: Reduced duplication, improved separation of concerns
- **Idiomatic Patterns**: Language-specific best practices (PEP8 for Python, modern ES/TS for JavaScript, etc.)
- **Error Handling**: Adds appropriate error handling and input validation
- **Documentation**: Adds helpful docstrings and comments where needed
- **Type Safety**: Adds type hints where appropriate (Python, TypeScript)
- **Code Style**: Consistent formatting and style conventions

## Supported File Extensions

- `.py` - Python
- `.js` - JavaScript
- `.ts` - TypeScript
- `.jsx` - JavaScript (React)
- `.tsx` - TypeScript (React)
- `.java` - Java
- `.kt` - Kotlin
- `.swift` - Swift

## Configuration

The refactoring behavior is controlled by a system prompt that emphasizes:
- Preserving behavior exactly
- Applying idiomatic patterns
- Improving clarity and maintainability
- Not introducing unnecessary dependencies
- Preserving important comments and TODOs

You can modify the `system_prompt` variable in the notebook to adjust the refactoring guidelines.

## Notes

- The tool preserves all external behavior and public APIs
- Original file structure and organization are maintained
- Important comments and TODOs are preserved
- The tool uses a low temperature (0.2) for consistent, deterministic refactoring
