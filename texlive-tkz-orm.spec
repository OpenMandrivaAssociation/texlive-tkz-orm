# revision 16849
# category Package
# catalog-ctan /graphics/pgf/contrib/tkz-orm
# catalog-date 2010-01-28 13:16:16 +0100
# catalog-license gpl
# catalog-version 0.1
Name:		texlive-tkz-orm
Version:	0.1
Release:	1
Summary:	Create Object-Role Model (ORM) diagrams,
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tkz-orm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides styles for drawing Object-Role Model (ORM)
diagrams in TeX based on the pgf and TikZ picture environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
