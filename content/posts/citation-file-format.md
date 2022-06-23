---
title: "CFF for Machine-Actionable Software Citations"
date: 2022-06-23T10:43:21-04:00
draft: false
---

Add a `CITATION.cff` file to your git repository. The [Citation File
Format](https://citation-file-format.github.io/) is automatically rendered on GitHub and usable by
Zenodo and Zotero.

Already have a DOI? [Let's see about a DOI-to-CFF
tool](https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench).
Looks like there's [doi2cff](https://github.com/citation-file-format/doi2cff), but it's currently
restricted to DOIs on Zenodo that are tagged as software releases.

So, this could work:
```
pip install git+https://github.com/citation-file-format/doi2cff
doi2cff init 10.5281/zenodo.6591863
```
```
CITATION.cff file has been written
```

Cool. But what if you want to cite something else? Let's go from DOI to BibTeX, and BibTeX to CFF.

Let's get BibTeX via [content negotiation](https://citation.crosscite.org/docs.html#sec-4):

```bash
curl -LH "Accept: application/x-bibtex" \
    https://doi.org/10.5281/zenodo.5570279 \
    >> refs.bib
```
```
# cat refs.bib
@article{https://doi.org/10.5281/zenodo.5570279,
  doi = {10.5281/ZENODO.5570279},
  url = {https://zenodo.org/record/5570279},
  author = {Canon, Shane and Christianson, Danielle and Duncan, William and Eloe-Fadrosh, Emiley and Fagnan, Kjiersten and Hays, David and Huntemann, Marcel and Lebedeva, Sofya and Miller, Kayd and Miller, Mark and Mouncey, Nigel and Mungall, Chris and Reddy, Tbk and Rudolph, Marisa and Sarrafan, Setareh and Sundaramurthi, Jagadish Chandrabose and Unni, Deepak and Vangay, Pajau and Wood-Charlson, Elisha and Ahmed, Faiza and Baumes, Jeffrey and Davis, Brandon and Anubhav, Fnu and Borkhum, Mark and Bramer, Lisa and Corilo, Yuri and Lipton, Mary and Mans, Douglas and McCue, Lee Ann and Millard, David and Piehowski, Paul and Prymolenna, Anastasiya and Purvine, Samuel and Richardson, Rachel and Smith, Montana and Stratton, Kelly and Babinski, Michal and Chain, Patrick and Davenport, Karen and Flynn, Mark and Hu, Bin and Kelliher, Julia and Li, Po-E and Lo, Chien-Chi and Jackson, Elais Player and Shakya, Migun and Xu, Yan and Drake, Meghan and Martin, Stanton and Wilson, Bruce and Winston, Donny},
  keywords = {microbiome, data science, data infrastructure, science gateway},
  title = {The National Microbiome Data Collaborative: a data science ecosystem for microbiome research},
  publisher = {Zenodo},
  year = {2021},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

Sweet. There is a command-line tool for [converting CFF to other common
formats](https://pypi.org/project/cffconvert/), but that's not what we want here. Ah, here we go:
[bibtex-to-cff](https://github.com/monperrus/bibtexbrowser/).

To save you a bit of hassle, I've packaged this PHP tool as a Docker image,
`polyneme/bibtex-to-cff`. Also, it can't (currently) handle URLs as BibTeX entry ids, so for this
case I changed `@article{https://doi.org/10.5281/zenodo.5570279,` in the above example to
`@article{10.5281.zenodo.5570279,` (it seems fine with periods).

Here goes:

```
docker run --rm \
    -v $(pwd):/usr/src/app/scratch \
    polyneme/bibtex-to-cff \
    scratch/refs.bib --id 10.5281.zenodo.5570279 \
    > CITATION.cff
```

Done. Add this to the root of your git repo, and congratulate yourself for including
machine-actionable citation metadata with your software.

You can build the image yourself by cloning the `monperrus/bibtexbrowser` GitHub repo, adding the
following to a new `Dockerfile` in the repo directory:

```Dockerfile
FROM php:7.4-cli
COPY . /usr/src/app
WORKDIR /usr/src/app
ENTRYPOINT [ "php", "bibtex-to-cff.php" ]
```
, and then `docker build -t bibtex-to-cff .`.

