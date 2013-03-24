Name: bozorth          
Version: 0.1       
Release:        1%{?dist}
Summary: C library and Java wrapper around bozorth3 fingerprint matcher      

License: Booz Allen Hamilton       
Source0: %{name}-%{version}.tar.gz       

BuildRequires: cmake NBIS
Requires: java      

%description


%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT
make
javac *.java
jar cvf bozorth.jar *.class

%install
rm -rf $RPM_BUILD_ROOT
make install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/*
%{_libdir}/*
%doc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%changelog
