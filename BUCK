python_binary(
    name = "run_bot",
    main = "bot.py",
    deps = [],
)

python_binary(
    name = "run_api",
    main = "api/server.py",
    deps = [],
)

genrule(
    name = "lint",
    out = "lint.log",
    cmd = "python3 -m flake8 . > $OUT",
)

genrule(
    name = "docker_build",
    out = "docker.done",
    cmd = "docker build -t minidyno . && touch $OUT",
)

genrule(
    name = "docker_run",
    out = "docker_run.done",
    cmd = "docker run -it --rm -p 8000:8000 minidyno && touch $OUT",
)
