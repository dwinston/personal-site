---
title: "A Delimiters-in-Front Coding Style"
date: 2021-09-03T10:41:01-04:00
draft: false
tags:
- code
---

When writing a multiline data structure literal, the usual convention is to put delimiters like
commas at the end of each line. For example, in Python:

```py
rules = [
  rule("Don't panic."),
  rule("Do NOT panic."),
  rule("No shouting.")
]
```

When you forget a comma, it's typically a syntax error and not difficult to debug:
```py
rules = [
  rule("Don't panic."),
  rule("Do NOT panic.")  # oops
  rule("No shouting.")
]
```

(This is why I like that Python allows one to have a trailing comma, which makes it less likely to
encounter this class of error when adding an element to the end of an existing  data structure
literal.)

In languages like Elm, missing commas may be harder to debug:
```elm
rules = [
  rule "Don't panic.",
  rule "Do NOT panic."  -- hmmm
  rule "No shouting."
]
```
gets interpreted as 
```elm
rules = [
   (rule "Don't panic."),
   (rule "Do NOT panic." rule "No shouting.")
]
```

, that is, as a list of two elements, with the second element being the result of a function call with
three supplied arguments.

Thus, in Elm, there is a convention of commas in front:[^1]

```elm
module PhotoGroove exposing (main)

import Html exposing (div, h1, img, text)
import Html.Attributes exposing (..)


view model =
    div [ class "content" ]
        [ h1 [] [ text "Photo Groove" ]
        , div [ id "thumbnails" ]
            [ img [ src "http://elm-in-action.com/1.jpeg" ] []
            , img [ src "http://elm-in-action.com/2.jpeg" ] []
            , img [ src "http://elm-in-action.com/3.jpeg" ] []
            ]
        ]


main =
    view "no model yet"
```

This style makes it easier for the eye to see that a comma is missing and to catch the error prior
to compile- or run-time.

Following the example of Elm style, I'm considering the value of a delimiters-in-front style for
hand-authored Turtle (terse triple format for RDF graph data). For example:

```turtle
@base <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sdo: <https://schema.org/> .

<pam> rdf:type sdo:Person
; rdfs:label "Pam"
; rdfs:comment "Works in a shop", "A go-getter"
.
<mrmustard> rdf:label "Mean Mister Mustard"
.
<mrmustard> rdf:comment "Sleeps in the park"
, "Shaves in the dark"
, "Such a mean old man"
.
<pam> sdo:sibling <mrmustard>
.
```
rather than a more conventional style, e.g.
```turtle
<pam> rdf:type sdo:Person ;
    rdfs:label "Pam" ;
    rdfs:comment "Works in a shop", "A go-getter" .
<mrmustard> rdf:label "Mean Mister Mustard" ;
    rdf:comment "Sleeps in the park",
                "Shaves in the dark",
                "Such a mean old man" .
<pam> sdo:sibling <mrmustard> .
```

I'm not aware of a set-it-and-forget-it reformat-on-save tool for `.ttl` files in the style of
`elm-format` for Elm or `black` for Python, both of which I love using. If I had that, I wouldn't
worry much about this because then a failure to reformat would be a sufficient visual signal that
I've done something wrong.

[^1]: R. Feldman, Elm in action. Shelter Island, NY: Manning Publications Co, 2020.