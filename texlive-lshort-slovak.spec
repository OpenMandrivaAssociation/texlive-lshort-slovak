Name:		texlive-lshort-slovak
Version:	15878
Release:	2
Summary:	Slovak introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/slovak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A Slovak translation of Oetiker's (not so) short introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-slovak/slshorte.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-slovak/src.zip

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
