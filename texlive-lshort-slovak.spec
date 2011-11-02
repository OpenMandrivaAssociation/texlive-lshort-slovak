Name:		texlive-lshort-slovak
Version:	20061230
Release:	1
Summary:	Slovak introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/slovak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A Slovak translation of Oetiker's (not so) short introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-slovak/slshorte.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-slovak/src.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
