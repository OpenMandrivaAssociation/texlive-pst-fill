%global tl_name pst-fill
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Fill or tile areas with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fill
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fill.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fill.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pst-fill is a PSTricks-based package for filling and tiling areas or
characters.

