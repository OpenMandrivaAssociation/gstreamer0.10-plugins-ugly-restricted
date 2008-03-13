%define version 0.10.7
%define release %mkrel 4
%define         _glib2          2.2
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define name %bname-plugins-ugly
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%define build_lame 0
%define build_amrnb 0

%if %build_plf
%define distsuffix plf
%define build_lame 1
%define build_amrnb 1
%endif

Summary: 	GStreamer Streaming-media framework plug-ins
Name: 		%name
Version: 	%version
Release: 	%release
License: 	LGPL
Group: 		Sound
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.bz2
#gw from CVS, fix for http://bugzilla.gnome.org/show_bug.cgi?id=518676
# (broken Xing VBR header)
Patch: gst-plugins-ugly-0.10.7-xing-header.patch
URL:            http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
#gw for the pixbuf plugin
BuildRequires:  gtk+2-devel
BuildRequires:  glib2-devel >= %_glib2 
BuildRequires: liboil-devel >= 0.3.2
BuildRequires: libgstreamer-plugins-base-devel >= %version
BuildRequires: libmesaglu-devel
BuildRequires: libmad-devel
BuildRequires: libid3tag-devel
BuildRequires: libdvdread-devel
BuildRequires: valgrind libcheck-devel
Provides:	%bname-audiosrc
Provides:	%bname-audiosink

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that have good quality and
correct functionality, but distributing them might pose problems. The
license on either the plug-ins or the supporting libraries might not
be how the GStreamer authors like. The code might be widely known to
present patent problems.

%if %build_plf
This package is in PLF as it violates some patents.
%endif


%prep
%setup -q -n gst-plugins-ugly-%{version}
cd gst/mpegaudioparse/
%patch

%build
%configure2_5x --disable-dependency-tracking \
%if %build_plf
  --with-package-name='PLF %name package' \
  --with-package-origin='http://plf.zarb.org/' \
%else
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
%endif
%if ! %build_lame
	--disable-lame \
%endif

%make

%check
cd tests/check
make check

%install
rm -rf %buildroot gst-plugins-base-%majorminor.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gst-plugins-ugly-%majorminor
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT



%files -f gst-plugins-ugly-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS
%_libdir/gstreamer-%majorminor/libgstasf.so
%_libdir/gstreamer-%majorminor/libgstdvdlpcmdec.so
%_libdir/gstreamer-%majorminor/libgstdvdread.so
%_libdir/gstreamer-%majorminor/libgstdvdsub.so
%_libdir/gstreamer-%majorminor/libgstiec958.so
%_libdir/gstreamer-%majorminor/libgstmad.so
%_libdir/gstreamer-%majorminor/libgstmpegaudioparse.so
%_libdir/gstreamer-%majorminor/libgstmpegstream.so
%_libdir/gstreamer-%majorminor/libgstrmdemux.so

%if %build_lame
### LAME ###
%package -n %bname-lame
Summary: GStreamer plug-in for encoding mp3 songs using lame
Group:  Sound
Requires: %bname-plugins >= %{version}
BuildRequires: liblame-devel >= 3.89

%description -n %bname-lame
Plug-in for encoding mp3 with lame under GStreamer.

This package is in PLF as it violates some patents.
%files -n %bname-lame
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%endif


%if %build_amrnb
%package -n %bname-amrnb
Summary: GStreamer plug-in for AMR-NB support
Group:  Sound
Requires: %bname-plugins >= %{version}
BuildRequires: libamrnb-devel

%description -n %bname-amrnb
Plug-in for decoding AMR-NB under GStreamer.

This package is in PLF as it violates some patents.
%files -n %bname-amrnb
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%endif


### SIDPLAY ###
%package -n %bname-sid
Summary: GStreamer Sid C64 music plugin
Group: Sound
Requires: %bname-plugins >= %{version}-%release
BuildRequires: sidplay-devel => 1.36.0
%description -n %bname-sid
Plugin for playback of C64 SID format music files

%files -n %bname-sid
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstsid.so


### A52DEC ###
%package -n %bname-a52dec
Summary: GStreamer VOB decoder plugin
Group: Sound
Requires: %bname-plugins >= %{version}-%release
BuildRequires: a52dec-devel >= 0.7.3

%description -n %bname-a52dec
Plugin for decoding of VOB files

%files -n %bname-a52dec
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so


### MPEG2DEC ###
%package -n %bname-mpeg
Summary:GStreamer plug-ins for MPEG video playback and encoding
Group:         Video
Requires:      %bname-plugins >= %{version}-%release
BuildRequires: libmpeg2dec-devel => 0.3.1

%description -n %bname-mpeg
Plug-ins for playing and encoding MPEG video.

%files -n %bname-mpeg
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so


