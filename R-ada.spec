%global packname  ada
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0.3
Release:          1
Summary:          ada: an R package for stochastic boosting
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ada_2.0-3.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-rpart 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-rpart
%rename R-cran-ada

%description
Performs discrete, real, and gentle boost under both exponential and
logistic loss on a given data set.  The package ada provides a
straightforward, well-documented, and broad boosting routine for
classification, ideally suited for small to moderate-sized data sets. 
Please refer to the Url below for more information.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0_2-1
+ Revision: 775013
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0_1-1
+ Revision: 774780
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-6mdv2011.0
+ Revision: 616444
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.0.1-5mdv2010.0
+ Revision: 433068
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-4mdv2009.0
+ Revision: 260119
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-3mdv2009.0
+ Revision: 248035
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix Url

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 169413
- import R-cran-ada


