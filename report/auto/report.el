(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "polyglossia"))
 :latex)

