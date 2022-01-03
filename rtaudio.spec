%define rtaudio _major 6
%define rtaudio %mklibname rtaudio %{rtaudio_major}
%define devname %mklibname -d usbmuxd

Summary:	Realttime audio	
Name:		rtaudio
Version:	5.2.0
Release:	1
License:	MIT
Group:		Audio
Url:		https://www.music.mcgill.ca/~gary/rtaudio/
Source0:	http://www.music.mcgill.ca/~gary/%{name}/release/%{name}-%{version}.tar.gz
#Patch0:		fix_cmake_install_paths.patch
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	doxygen
BuildRequires:	cmake

%description
A set of C++ classes that provide a common API for realtime audio input/output 
for Linux (native ALSA, JACK, PulseAudio and OSS)

%files
%{_libdir}/librtaudio.so.*


%doc README.md

%package devel
Summary:	Development files for %{name}
Group:		Development/Audio
Provides:	librtaudio-devel = %{EVRD}
Requires:	rtaudio = %{EVRD}

%description devel
Development files for %{name}

%files devel
%{_includedir}/%{name}/*.h
%{_includedir}/*.h
%{_libdir}/librtaudio.so
%{_libdir}/pkgconfig/*
%{_datadir}/%{name}/*.cmake
%doc doc/html/

#--------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir}

%make_build

cd %{_builddir}/%{name}-%{version}/doc/doxygen; doxygen  Doxyfile.in


%install
mkdir -p %{buildroot}%{_includedir}/rtaudio
cp RtAudio.h %{buildroot}%{_includedir}/rtaudio/
cp rtaudio_c.h %{buildroot}%{_includedir}/rtaudio/

%make_install -C build
#mv RtAudio.h %{buildroot}%{_includedir}/rtaudio/
