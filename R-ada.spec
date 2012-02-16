%global packname  ada
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0_2
Release:          1
Summary:          ada: an R package for stochastic boosting
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-2.tar.gz
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
