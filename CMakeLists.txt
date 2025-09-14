cmake_minimum_required(VERSION 3.15)
project(MiniDyno VERSION 1.0.0 LANGUAGES NONE)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

add_custom_target(run_bot
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/bot.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🚀 Running MiniDyno Discord Bot"
)

add_custom_target(run_api
    COMMAND ${Python3_EXECUTABLE} -m uvicorn api.server:app --reload
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🌐 Running MiniDyno API"
)

add_custom_target(lint
    COMMAND ${Python3_EXECUTABLE} -m flake8 ${CMAKE_SOURCE_DIR}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🔍 Linting MiniDyno Python code"
)

add_custom_target(docker_build
    COMMAND docker build -t minidyno ${CMAKE_SOURCE_DIR}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🐳 Building MiniDyno Docker image"
)

add_custom_target(docker_run
    COMMAND docker run -it --rm -p 8000:8000 minidyno
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🐳 Running MiniDyno container"
)
