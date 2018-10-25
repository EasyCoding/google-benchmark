%global intname benchmark
%global lbname lib%{intname}

Name: google-benchmark
Version: 1.4.1
Release: 1%{?dist}

License: ASL-2.0
Summary: A microbenchmark support library
URL: https://github.com/google/%{intname}
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{intname}-%{version}
mkdir -p %{_target_platform}
sed -i 's@lib/@%{_lib}/@g' src/CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files
%doc AUTHORS CONTRIBUTORS CONTRIBUTING.md README.md
%license LICENSE
%{_libdir}/%{lbname}*.so.0*

%files devel
%{_libdir}/%{lbname}*.so
%{_includedir}/%{intname}
%{_libdir}/cmake/%{intname}
%{_libdir}/pkgconfig/%{intname}.pc

%changelog
* Thu Oct 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.1-1
- Initial SPEC release.
