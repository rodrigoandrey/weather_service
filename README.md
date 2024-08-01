FASTAPI WEATHER SERVICE
===============================
## This simple web app was made for training purposes

Dependencies
===============================

- Python==3.12.*, fastapi, uvicorn, httpx, pytest, pytest-cov
- Docker (https://www.docker.com/products/docker-desktop)
  - Windows Tutorial: https://docs.docker.com/desktop/install/windows-install/
  - Linux Tutorial: https://docs.docker.com/desktop/install/linux-install/
  - MacOS Tutorial: https://docs.docker.com/desktop/install/mac-install/
- API key from: OpenWeatherMap (https://openweathermap.org/)

Running
===============================
- Clone or download the project.
- Set up your virtual environment venv using Python==3.12.* (e.g., python3 -m venv venv) and activate your venv.
- If you don't know how to set up a venv and how to activate it, here's a quick tutorial:
  - https://dev.to/shriekdj/how-to-create-and-activate-the-virtual-environment-for-python3-project-3g4l
- Navigate to the root of the project and install requirements.txt
  - `pip install -r requirements.txt`
- Create a .env file in the root folder of the project with the following content:
  - OWM_API_KEY=your_openweathermap_api_key_here
- In the root folder with your venv activated, run the following command: 
  - `fastapi dev main.apy`
- The application will run in development mode. For production use: 
  - `fastapi run`
- You can access the application through the address displayed
  - http://127.0.0.1:8000 or http://localhost:8000

Running with Docker
===============================
- Clone or download the project.
- Create a `.env file` in the project's `root folder` with the following content:
  - OWM_API_KEY=your_openweathermap_api_key_here
- Install and set up `docker | docker-desktop`.
  - In some cases, it's necessary on Windows | MacOS to keep the Docker Desktop app running.
- On `terminal | cmd`, navigate to the `root folder` of the project and run the following command: 
  - `docker build -t weather_service .`
- Wait until the process finishes.
- Wait until the process finishes the run the following command: 
  - `docker run -d -p 8000:8000 weather_service`
- You can access the application through the address 
  - http://127.0.0.1:8000 or http://localhost:8000

Testing
===============================
- With `venv activated`, navigate to the `root of the project`.
- Run the following command: 
  - `pytest`

Usage
===============================
- You can check the documention for the `endpoints` in the following link:
  - http://127.0.0.1:8000/docs or http://localhost:8000/docs