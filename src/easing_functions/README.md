# Plot Easing Funcs

I wanted a local script to produce the plots/charts/graphs that Disco Diffusion notebooks have added recently.

This script does that.

It reads an array of schedules from `./schedules.json` and produces a plot output to the `Path` attribute.

## schedules.json reference

> Path is a relative path from the root of this repo

```json
[
    {
        "DisplayName":   "Title for Plot",
        "Path":          "path/to/output/filename.png",
        "cut_easing_fn": "CubicEaseInOut",
        "cut_overview":  "[23]*100+dd_easing_int(start=23, end=1, steps=800, easing_fn=cut_easing_fn)+[1]*100",
        "cut_innercut":  "[1]*100+dd_easing_int(start=1, end=23, steps=800, easing_fn=cut_easing_fn)+[23]*100",
        "cut_ic_pow":    "dd_easing_float(start=10, end=1, steps=1000, easing_fn=cut_easing_fn)",
        "cut_icgray_p":  "[0.6]*100+[0.2]*100+[0.1]*100+[0.05]*100+[0]*600"
    }
]
```

## Install

From repo root:

```terminal
make install-plots
```

## Usage

From repo root:

```terminal
make plots
```
