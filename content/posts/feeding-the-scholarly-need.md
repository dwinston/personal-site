---
title: "Feeding the Scholarly Need"
date: 2024-04-08T10:49:37-04:00
draft: false
tags:
  - scholarly
---

This post marks the re-introduction of [a feed for each tag](/posts/tag-test/) on this blog.

I want this so that I can post without worrying about contributing to "pollution" of the scholarly record.
I can accomplish this by tagging posts as `#scholarly` when I want them to be e.g.
fetched by [The Rogue Scholar](https://rogue-scholar.org/) for [DOI](https://www.doi.org/) minting
and for subsequent linking to my [ORCiD](https://orcid.org/) profile.

This post should hopefully be my last act of such pollution. 🙂

For this [Hugo](https://gohugo.io)-based blog, I accomplished this by creating a `layouts/tags/term.atom.xml` file
with this content:

```xml
{{ $taxo := "tags" }}
{{- $pages := .RegularPages  -}}
{{- with .Site.Config.Services.RSS.Limit -}}
  {{- if ge . 1 -}}
    {{- $pages = $pages | first . -}}
  {{- end -}}
{{- end -}}
{{ print "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>" | safeHTML }}
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:webfeeds="http://webfeeds.org/rss/1.0">
  <author>
    <name>{{ .Site.Author.name }}</name>
    <uri>{{ .Site.Author.orcid }}</uri>
  </author>
  <generator uri="https://gohugo.io">Hugo {{ .Site.Hugo.Version }}</generator>
  <id>{{ if .Site.Params.feedUUID }}urn:uuid:{{.Site.Params.feedUUID }}{{ else }}{{ .Permalink }}{{ end }}</id>
  {{ with .OutputFormats.Get "atom" }}
  {{ printf `<link rel="self" type="%s" href="%s" hreflang="%s"/>` .MediaType.Type .Permalink $.Site.LanguageCode | safeHTML }}
  {{ end }}
  {{ range .AlternativeOutputFormats }}
  {{ printf `<link rel="alternate" type="%s" href="%s" hreflang="%s"/>` .MediaType.Type .Permalink $.Site.LanguageCode | safeHTML }}
  {{ end }}
  {{ with .Site.Params.icon }}<icon>{{ . | absURL }}</icon>{{ end }}
  {{ with .Site.Params.logo }}<logo>{{ . | absURL }}</logo>{{ end }}
  {{ with .Site.Copyright }}<rights>{{ replace . "{year}" now.Year }}</rights>{{ end }}
  {{ with .Site.Params.Description }}<subtitle>{{ .  }}</subtitle>{{ end }}
  <title>{{ .Site.Title }} - posts tagged "{{ .Data.Term }}" </title>
  <updated>{{ now.Format .Site.Params.dateFormatAtomFeed | safeHTML }}</updated>
  {{ with .Site.Params.icon96 }}<webfeeds:icon>{{ . | absURL }}</webfeeds:icon>{{ end }}
  {{ range $pages }}
  <entry>
    <author>
    {{ if .Params.author }}
      <name>{{ .Params.author.name }}</name>
      <uri>{{ .Params.author.orcid }}</uri>
    {{ else }}
      <name>{{ .Site.Author.name }}</name>
      <uri>{{ .Site.Author.orcid }}</uri>
    {{ end }}
    </author>
    <id>tag:{{ $u := urls.Parse .Permalink }}{{ $u.Hostname }},{{ .Date.Format .Site.Params.dateFormatTag }}:{{ replace $u.Path "#" "_" }}</id>
    <link rel="alternate" href="{{ .Permalink }}"/>
    <title>{{ .Title }}</title>
    <published>{{ .Date.Format .Site.Params.dateFormatAtomFeed | safeHTML }}</published>
    <updated>{{ .Lastmod.Format .Site.Params.dateFormatAtomFeed | safeHTML }}</updated>
    {{ with .Description }}<summary type="text">{{ . }}</summary>{{ end }}
    <content type="html" xml:base="{{ .Site.BaseURL }}" xml:lang="en">
      {{ printf "<![CDATA[%s]]>" .Content | safeHTML }}
    </content>
  </entry>
  {{ end }}
</feed>
```

And here is my revised `hugo.toml` site configuration:

```toml
baseURL = ""
copyright = "Copyright © 2020-{year} Donny Winston. All posts licenced under <https://creativecommons.org/licenses/by-nc-sa/4.0/>."
languageCode = "en-us"
rssLimit = 100
title = "Donny Winston"
timeZone = "America/New_York"
theme = "noteworthy"
enableRobotsTXT = true
paginate = 4
summaryLength = 10

[taxonomies]
  tag = "tags"

[author]
	name = "Donny Winston"
    orcid = "https://orcid.org/0000-0002-8424-0604"

# Set to false to disallow raw HTML in markdown files
[markup.goldmark.renderer]
    unsafe = true

[mediaTypes]
  [mediaTypes."application/atom+xml"] # Thank you <https://c20d.blog/posts/2023/04/atom-feeds-with-hugo/> !
    suffixes = ["xml"]

# Menu links along the sidebar navigation.
[[menu.main]]
	identifier = "about"
	name = "About"
	url = "/about/"
	weight = 1 # Weight is an integer used to sort the menu items. The sorting goes from smallest to largest numbers. If weight is not defined for each menu entry, Hugo will sort the entries alphabetically.

[[menu.main]]
	identifier = "consulting"
	name = "Consulting"
	url = "/consulting/"
	weight = 2

#[[menu.main]]
#	identifier = "tags"
#	name = "Tags"
#	url = "/tags/"
#	weight = 3

[[menu.main]]
	name = "Archives"
	identifier = "archives"
	url = "/archives/"
	weight = 4

[[menu.main]]
	identifier = "feed"
	name = "Feed"
	url = "/feed.xml"
	weight = 5

[outputFormats]
  [outputFormats.ATOM]
    mediaType = "application/atom+xml"
    baseName  = "feed"

[outputs]
  home = ["ATOM", "HTML"]
  page = ["HTML"]
  section = ["HTML"]
  taxonomy = ["HTML"]
  term = ["ATOM", "HTML"]

[params]
    favicon = "https://files.polyneme.xyz/polyneme-logo-sq-AdH548JPkxW0qf3M5NVTVLt5qdVKFN28AKKvS35A2ndmDMQ0baH90H5APJvIITO2UkFht8rLzZGQTxob8DCqG3KqnsEOczShPKoT.png"
	math = true
	# Blog description at the top of the homepage. Supports markdown.
	description = "Made as simple as possible, but not simpler."

    # Set enableKofi to true to enable the Ko-fi support button. Add your Ko-fi ID to link to your account.
    enableKofi = false
    kofi = ""

	# Add links to your accounts. Remove the ones you don't want to include.
	# Main
	# email = "mailto:donny@donnywinston.com"
	linkedin = "https://www.linkedin.com/in/donnywinston/"

	# Programming
    github = "https://github.com/dwinston/"
	# stackoverflow = "#"

    # Academic
    # googlescholar = "#"
    orcid = "https://orcid.org/0000-0002-8424-0604"

    mastodon = "https://fairpoints.social/@donny"

    dateFormatAtomFeed = "2006-01-02T15:04:05-07:00"
    dateFormatTag = "2006"
    feedUUID = "390a272f-8fa2-425a-b44e-09b477223a39"
    icon = "https://files.polyneme.xyz/polyneme-logo-sq-AdH548JPkxW0qf3M5NVTVLt5qdVKFN28AKKvS35A2ndmDMQ0baH90H5APJvIITO2UkFht8rLzZGQTxob8DCqG3KqnsEOczShPKoT.png"
    icon96 = "https://files.polyneme.xyz/polyneme-logo-sq-AdH548JPkxW0qf3M5NVTVLt5qdVKFN28AKKvS35A2ndmDMQ0baH90H5APJvIITO2UkFht8rLzZGQTxob8DCqG3KqnsEOczShPKoT.png"
    logo = "https://files.polyneme.xyz/polyneme-logo-sq-AdH548JPkxW0qf3M5NVTVLt5qdVKFN28AKKvS35A2ndmDMQ0baH90H5APJvIITO2UkFht8rLzZGQTxob8DCqG3KqnsEOczShPKoT.png"
    mainSections = ["posts"]

# Privacy configurations: https://gohugo.io/about/hugo-and-gdpr/
[privacy]
  [privacy.disqus]
    disable = true
  [privacy.googleAnalytics]
    disable = true
  [privacy.instagram]
    disable = true
  [privacy.twitter]
    disable = true
  [privacy.vimeo]
    disable = true
  [privacy.youtube]
    disable = true
```

Furthermore, I am testing references introspection [^rsrefs] with this post.


[^rsrefs]: Fenner, Martin. “Starting to Include References in DOI Metadata for Blog Posts.” Front Matter, June 16, 2023. https://doi.org/10.53731/6mkrk-dzh02.
