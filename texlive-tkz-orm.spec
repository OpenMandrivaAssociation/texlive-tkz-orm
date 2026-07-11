%global tl_name tkz-orm
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.4
Release:	%{tl_revision}.1
Summary:	Create Object-Role Model (ORM) diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tkz-orm
License:	gpl2 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-orm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides styles for drawing Object-Role Model (ORM) diagrams
in TeX based on the PGF and TikZ picture environment.

