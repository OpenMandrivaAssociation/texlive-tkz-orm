Name:		texlive-tkz-orm
Version:	61719
Release:	2
Summary:	Create Object-Role Model (ORM) diagrams,
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tkz-orm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides styles for drawing Object-Role Model (ORM)
diagrams in TeX based on the pgf and TikZ picture environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-orm/tkz-orm.sty
%doc %{_texmfdistdir}/doc/latex/tkz-orm/LICENSE
%doc %{_texmfdistdir}/doc/latex/tkz-orm/Makefile
%doc %{_texmfdistdir}/doc/latex/tkz-orm/README
%doc %{_texmfdistdir}/doc/latex/tkz-orm/pgfmanualstyle.sty
%doc %{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.bib
%doc %{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-orm/tkz-orm.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
