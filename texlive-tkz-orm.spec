# revision 16849
# category Package
# catalog-ctan /graphics/pgf/contrib/tkz-orm
# catalog-date 2010-01-28 13:16:16 +0100
# catalog-license gpl
# catalog-version 0.1
Name:		texlive-tkz-orm
Version:	0.1
Release:	8
Summary:	Create Object-Role Model (ORM) diagrams,
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tkz-orm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 756997
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719768
- texlive-tkz-orm
- texlive-tkz-orm
- texlive-tkz-orm

