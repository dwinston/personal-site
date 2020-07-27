---
title: "Feedback Needs an Output"
date: 2020-07-27T17:00:27-04:00
draft: false
---

Feedback taken without knowing the specific outcome it will be used to adjust, is not feedback.
It may be input of some sort, but for what system? What does it feed? To what does it link?

Below is a schematic of well-defined feedback. An operational amplifier is shown using feedback in
order to produce output with a closed-loop gain of \\(1 + \frac{R_f}{R_g}\\). That is, \\(V_{out} = (1 + \frac{R_f}{R_g})V_{in}\\).

<a title="Ong saluri / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" href="https://commons.wikimedia.org/wiki/File:Operational_amplifier_noninverting.svg"><img width="256" alt="Operational amplifier noninverting" src="https://upload.wikimedia.org/wikipedia/commons/6/66/Operational_amplifier_noninverting.svg"></a>

Feedback in a system needn't be *live* like in the op amp above. There may be an asynchronous processing/integration step, but
unambiguous links must be in place.