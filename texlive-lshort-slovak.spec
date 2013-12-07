# revision 15878
# category Package
# catalog-ctan /info/lshort/slovak
# catalog-date 2006-12-30 01:42:23 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-lshort-slovak
Version:	20061230
Release:	3
Summary:	Slovak introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/slovak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-slovak.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061230-2
+ Revision: 753481
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061230-1
+ Revision: 718901
- texlive-lshort-slovak
- texlive-lshort-slovak
- texlive-lshort-slovak
- texlive-lshort-slovak

