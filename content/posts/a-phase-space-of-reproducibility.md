---
title: "A Phase Space of Reproducibility"
date: 2022-05-09T12:29:56-04:00
draft: false
---

![Phase Space of Reproducibility](https://files.polyneme.xyz/dropshare/reproducibility-phase-space-wSnbNlvjVR.png)

What does "reproducible science" encompass?

## A tug-of-war

Here is one decomposition into "repeatability", "reproducibility", and "replicability":[^acm]
> "Repeatability (Same team, same experimental setup)...Reproducibility (Different team, same experimental setup)...Replicability (Different team, different experimental setup)..."

Here is a conflicting account of the relationship between "replicability" and "reproducibility":[^grad]
> "...even if we can replicate the results of a paper, slightly altering the experimental setup could have dramatically different results. For these reasons, we don’t want to consider the authors code, as this could be a source of bias. We want to focus on the question of reproducibility, without wading into the murky waters of replication."

It seems that ACM's "replicability" is Edward Raff's "reproducibility", and vice versa. And the colloquial phrase "repeat after me" is at odds with ACM's "repeatability".

## A trip to the dictionary

Merriam-Webster[^mw] defines reproduction as
> the process by which plants and animals give rise to offspring and which fundamentally consists of the segregation of a portion of the parental body by a sexual or an asexual process and its subsequent growth and differentiation into a new individual.

and reports the first known use in circa 1640, in the above sense.

So, it seems to me that reproduction subsumes replication — replication is a sub-type of reproduction where, subjective to an observer, the new individual is a replica — an indistinguishable image — of the parental body.

Repetition seems like the kind of reproduction where no material portion of a parental body is involved. “Repeat after me” is about a second agent observing the first agent and reproducing the output of the first agent without material reuse of a portion of the first agent’s material output.

Repetition is about following the same method but without using a seed from the original performance.

Reproduction of result, i.e. growth of a new individual, can occur / be attempted with or without repetition of method. With or without repeated method, the growth of a new individual from the seed may or may not be successful.

## Repetition of methods, replication of results

Repetition seems method-focused (same activities) whereas replication seems result-focused (same outcomes).

A reproduction can be perceived as more or less a repetition of the original production activities, and can orthogonally be perceived as more or less a replication of the original production outcomes.

## Reproduction = Representation + Repetition + Replication

In terms of the W3C Provenance ontology's[^prov] core types of Agent, Activity, and Entity (diagram at top reproduced here):

![Phase Space of Reproducibility](https://files.polyneme.xyz/dropshare/reproducibility-phase-space-wSnbNlvjVR.png)

Reproducibility is the space. One axis is repeatability, i.e. “activity-dependent reproducibility”. Another axis is replicability, i.e. “entity-dependent reproducibility”. The final axis is “agent-dependent reproducibility”. For scientific reproducibility, we really (really) would like to ignore the Agent axis — sure, agent/representative identity is correlated with entity resourcing and activity resourcing capacity and skill in the real world, but we’d rather not consider it an independent axis.

Thus, we consider a scientific process reproducible in part by its repeatability (reproduction of activities) and its replicability (reproduction of entities - artifacts, results, outcomes). This seems subjective, But “up and to the right” in the figure above is what we seem to seek.

## How repeatable is reproduction? How replicable is it?

Engineering emphasizes modeling for prediction, whereas science emphasizes modeling for explanation. Thus, while repeatability (same activities) may not be valued for outcome-focused reproducibility in engineering, repeatability is valued for activity-focused reproducibility in science, that is, for explainability in terms of causes and conditions.

## On independent reproduction

While we can consciously seek repeatability and replicability in reproduction attempts, we also typically value so-called “independent” reproduction, where it seems the investigating agent(s) were either not aware of original activities or of original starter/intermediate/output entities, or both, and yet reproduced them anyhow.

The significance of independent reproduction is not so much for validity of reproduction as it is for assigning credit to discovery, but still, independent reproduction is often perceived as more valid due to a perceived reduction in risk of dishonest reporting.

[^acm]: “Artifact Review and Badging - Current.” Association for Computing Machinery. https://www.acm.org/publications/policies/artifact-review-and-badging-current (accessed May 09, 2022).

[^grad]: E. Raff, "Quantifying independently reproducible machine learning," The Gradient, Feb. 2020, [Online]. Available: https://thegradient.pub/independently-reproducible-machine-learning/

[^mw]: “Definition of REPRODUCTION.” https://www.merriam-webster.com/dictionary/reproduction (accessed May 09, 2022).

[^prov]: “PROV-DM: The PROV Data Model.” W3C Recommendation, April 30, 2013. https://www.w3.org/TR/prov-dm/ (accessed May 09, 2022).

{{< subscribe >}}