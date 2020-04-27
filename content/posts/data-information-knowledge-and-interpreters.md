---
title: "Interpreting Data→Information→Knowledge"
date: 2020-04-23T11:53:31-04:00
draft: false
---
 
 > There is a lot of data out there that many of you can turn into information. Synthesizing the information into
 knowledge takes experience and help. And utilizing knowledge until it’s innate wisdom it [*sic*] harder still.
> 
> &mdash; <cite>Alan Weiss</cite>[^0]

I'd like have a working mental model for this chain relating data, information, knowledge, and wisdom.
Weiss and Wilkerson define data, information, knowledge, and wisdom as follows[^1]:
> Data - units of statistics, numbers, words, and language that can be gathered and sorted.
> <br><br>
> Information - facts derived from data that can be verified and validated.
> <br><br>
> Knowledge - information combined with one’s talents that creates a grasp of subject matter, context, and
> application.
> <br><br>
> Wisdom - information [*sic*] combined with judgement and experience to anticipate and apply solutions and make quality
> decisions.

The above is a helpful starting point for me, but it falls short in two ways. First, it unnecessarily complicates by
 branching both knowledge and wisdom from information. This is why I included the "[*sic*]" above. Let's take it to
  read that wisdom is *knowledge* combined with judgement and experience.
  
The second way the definitions above fall short is best expressed by Fong and Spivak's co-definition of data and
 information[^2]:

> Data becomes information when it is stored *in* a given *formation*.
> That is, the numbers and letters don’t mean anything until they are organized,
> often into a system of interlocking tables.
> An organized system of interlocking tables is called a database.

Thus, information is the "gathered" state of that which "can be gathered". To turn information into
"facts" (which are not "facts" *until* they are "verified and validated") is to apply a grasp of subject matter
 and context.
 
I also see how information and knowledge can get complected[^hickey], given common usage of the term "informative".
In *The Goal*,[^3] database analyst Ralph
 draws a distinction between data and information that aligns
 with Wilkerson and Weiss' distinction one rung up the ladder, between information and knowledge:
> What I’m holding in my files is data. What you are usually asking for is information. I always regarded information
 as those sections of the data which are needed in order to make a decision...What I started to realize is that
> information is something else. Information is the answer to the question asked.

## The Structure and Interpretation of Data

Now that I've somewhat explicated the terms of the chain of data-information-knowledge-wisdom, I'm ready to reify it
 by way of analogy to the structure and interpretation of computer programs (not to the book itself,[^sicp] but
  certainly to its contents!).

The road from data to information is akin to the traditional
 decomposition of 
 discovering the structure of a program's text into two subtasks[^lexyacc]:
> 1. Split the source file into tokens (Lex).
> 2. Find the hierarchical structure of the program (Yacc).

Take, for instance, this simple source text: `[1, 3, 5, 7, 9]`. A tokenizer could take that source and produce
 this stream of tokens, of data: 
 `[`, `1`, `,` (the comma token), `3`, `,`, `5`, `,`, `7`, `,`, `9`, and finally `]`.
 Then, a parser could take a pass at the token data, getting them *in formation*, interpreted as a list data
  structure
  with five numeric elements. In this way, data (tokens) sourced from text
  are gathered in formation as the program's abstract syntax tree (AST).
  
How, now, to combine information, to "grasp" its context for application? How to go from information to knowledge?
The *environment model of evaluation* reifies the idea of context and its application to information[^sicp]:
> The environment is crucial to the evaluation process, because it determines the context in which an expression should be evaluated. Indeed, one could say that expressions in a programming language do not, in themselves, have any meaning. Rather, an expression acquires a meaning only with respect to some environment in which it is evaluated. Even the interpretation of an expression as straightforward as (+ 1 1) depends on an understanding that one is operating in a context in which + is the symbol for addition.

The environment model involves "frames" that each host a set of variable-value bindings, like a variable `x` being bound
 to the numeric value `3`. Each frame may point to an enclosing ("backup") frame. The evaluation process
  follows a sequence of frames to find the appropriate value to give to a variable. The right value depends on the
   current arrangement of frames and their contents, which changes as the program steps in and out of new local
    frames of execution.

Philip Guo's Python Tutor[^pytutor] is a great tool to visualize the knowledge
     structure of program execution, the evolving environment-frame structure and its application to information
      (object data structure).
      
Stephen Wolfram also connects knowledge representation with computation. From his announcement of RDF
 and SPARQL support
 in the latest major release of Mathematica[^wolfram]:
 > What is the best way to represent knowledge about the world? It’s an issue that’s been debated by philosophers (and others) since antiquity. Sometimes people said logic was the key. Sometimes mathematics. Sometimes relational databases. But now we at least know one solid foundation (or at least, I’m pretty sure we do): everything can be represented by computation.

Finally, where does *wisdom* fit in? It doesn't. It fits *out*, outside the program interpreter, guiding its execution.
Wisdom is embedded in the person who
assembles appropriate source data and program syntax *in formation* and runs it on a machine in a certain context.
Wisdom compiles in you.

[^0]: Alan Weiss, https://alanweiss.com/consulting-wisdom/, 2009.
[^1]: Wilkerson and Weiss, *The Language of Success*. Business Expert Press, 2015.
[^2]: Fong and Spivak, *Seven Sketches in Compositionality: An Invitation to Applied Category Theory*. arXiv, 2018.
[^hickey]: To interleave, entwine, braid.
<br>See also: Hickey, "Simple Made Easy." Strange Loop, 2011.
[[transcript](https://github.com/matthiasn/talk-transcripts/blob/9f33e07ac392106bccc6206d5d69efe3380c306a/Hickey_Rich/SimpleMadeEasy.md)]
[^3]: Goldratt and Cox, *The Goal: A Process of Ongoing Improvement*. North River Press, 1992.
[^sicp]: Abelson and Sussman, *Structure and Interpretation of Computer Programs*. MIT Press, 1996.
[^lexyacc]: "The Lex & Yacc Page", <http://dinosaur.compilertools.net/>.
<br>See also: Levine, Mason, and Brown, *Lex & Yacc*. O'Reilly, 1992.
[^pytutor]: Guo, "Online Python Tutor: Embeddable Web-Based Program Visualization for CS Education," ACM Technical
 Symposium on Computer Science Education (SIGCSE), 2013. <http://pythontutor.com/>
 [^wolfram]: Wolfram, "Version 12 Launches Today!", 2019.<br>
 [[section on "RDF, SPARQL and All That"](https://writings.stephenwolfram.com/2019/04/version-12-launches-today-big-jump-for-wolfram-language-and-mathematica/#rdf-sparql-and-all-that)]