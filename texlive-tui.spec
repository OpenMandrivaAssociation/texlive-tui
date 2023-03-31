Name:		texlive-tui
Version:	27253
Release:	2
Summary:	Thesis style for the University of the Andes, Colombia
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tui
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tui.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tui.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Doctoral Dissertations from the Faculty of Engineering at the
Universidad de los Andes, Bogota, Colombia. The class is
implemented as an extension of the memoir class. Clase de Tesis
doctorales para ingenieria, Universidad de los Andes, Bogota.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tui/tui.cls
%doc %{_texmfdistdir}/doc/latex/tui/README
%doc %{_texmfdistdir}/doc/latex/tui/TUIdoc.pdf
%doc %{_texmfdistdir}/doc/latex/tui/TUIdoc.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/abstract.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/agradec.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/ap01.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/bibliotesis.bib
%doc %{_texmfdistdir}/doc/latex/tui/example/ch01.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/ch02.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/ch03.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/coleccion.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/dedicat.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/hyphenation.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/imagen.pdf
%doc %{_texmfdistdir}/doc/latex/tui/example/intro.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/lipsum.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/listofsymbols.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/main.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/plegal.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/portada.tex
%doc %{_texmfdistdir}/doc/latex/tui/example/resumen.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/abstract.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/agradec.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/ap01.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/bibliotesis.bib
%doc %{_texmfdistdir}/doc/latex/tui/template/ch01.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/ch02.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/ch03.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/coleccion.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/dedicat.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/hyphenation.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/intro.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/listofsymbols.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/main.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/plegal.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/portada.tex
%doc %{_texmfdistdir}/doc/latex/tui/template/resumen.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
