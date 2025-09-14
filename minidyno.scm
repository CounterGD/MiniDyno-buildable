(define-module (minidyno package))
(use-modules (guix packages)
             (guix download)
             (guix build-system python)
             (gnu packages python)
             (gnu packages docker))

(define-public minidyno
  (package
    (name "minidyno")
    (version "1.0.0")
    (source (local-file "." "minidyno-src"))
    (build-system python-build-system)
    (inputs
      (list python python-pip docker))
    (synopsis "MiniDyno Discord Moderation Bot")
    (description "A Discord moderation bot with API, dashboard, and multi-builder support.")
    (home-page "https://github.com/minidyno")
    (license license:expat)))
