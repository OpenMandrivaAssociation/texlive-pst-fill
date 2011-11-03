# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fill
# catalog-date 2007-03-11 15:39:31 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-pst-fill
Version:	1.01
Release:	1
Summary:	Fill or tile areas with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fill
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fill.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fill.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fill.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Pst-fill is a PSTricks-based package for filling and tiling
areas or characters.

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
%{_texmfdistdir}/tex/generic/pst-fill/pst-fill.tex
%{_texmfdistdir}/tex/latex/pst-fill/pst-fill.sty
%doc %{_texmfdistdir}/doc/generic/pst-fill/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fill/README
%doc %{_texmfdistdir}/doc/generic/pst-fill/pst-fill.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-fill/Makefile
%doc %{_texmfdistdir}/source/generic/pst-fill/pst-fill.dtx
%doc %{_texmfdistdir}/source/generic/pst-fill/pst-fill.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}