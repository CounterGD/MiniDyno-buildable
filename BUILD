py_binary(
    name = "run_bot",
    srcs = ["bot.py"],
    deps = [],
)

py_binary(
    name = "run_api",
    srcs = ["api/server.py"],
    deps = [],
)

genrule(
    name = "lint",
    outs = ["lint.log"],
    cmd = "python3 -m flake8 . > $@",
)

genrule(
    name = "docker_build",
    outs = ["docker.done"],
    cmd = "docker build -t minidyno . && touch $@",
)

genrule(
    name = "docker_run",
    outs = ["docker_run.done"],
    cmd = "docker run -it --rm -p 8000:8000 minidyno && touch $@",
)
