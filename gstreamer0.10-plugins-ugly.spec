%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%define build_experimental 0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_lame 0
%define build_amrnb 0
%define build_amrwbdec 0
%define build_x264 0

######################################33
# Hardcode PLF build
%define build_plf 1
######################################33

%if %{build_plf}
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define build_lame 1
%define build_x264 1
%define build_amrnb 1
%define build_amrwbdec 1
%endif

%define oname	gst-plugins-ugly
%define api	0.10
%define bname	gstreamer%{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-ugly
Version:	0.10.19
Release:	3%{?extrarelsuffix}
License:	LGPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{oname}-%{version}.tar.xz
Patch0:		gstreamer-plugins-ugly-0.10.17-amr-linking.patch
Patch1:		gst-plugins-ugly-0.10.19-opencore.patch
Patch2:		gst-plugins-ugly-0.10.19-cdio90.patch

BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(orc-0.4)
%ifnarch %{mips} %{arm}
BuildRequires:	valgrind
%endif
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink

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

%if %{build_plf}
This package is in restricted as it violates some patents.
%endif

%if %{build_lame}
### LAME ###
%package -n %{bname}-lame
Summary:	GStreamer plug-in for encoding mp3 songs using lame
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	%{bname}-plugins-base
BuildRequires:	lame-devel >= 3.89

%description -n %{bname}-lame
Plug-in for encoding mp3 with lame under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-lame
%{_libdir}/gstreamer-%{api}/libgstlame.so
%endif

%if %{build_x264}
%package -n %{bname}-x264
Summary:	GStreamer plug-in for H264/AVC video encoding
Group:		Video
BuildRequires:	x264-devel

%description -n %{bname}-x264
Plug-in for encoding H264/AVC video.

This package is in restricted as it violates some patents.

%files -n %{bname}-x264
%{_libdir}/gstreamer-%{api}/libgstx264.so
%{_datadir}/gstreamer-%{api}/presets/GstX264Enc.prs
%endif

%if %{build_amrnb}
%package -n %{bname}-amrnb
Summary:	GStreamer plug-in for AMR-NB support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(opencore-amrnb)

%description -n %{bname}-amrnb
Plug-in for decoding AMR-NB under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-amrnb
%{_libdir}/gstreamer-%{api}/libgstamrnb.so
%{_datadir}/gstreamer-%{api}/presets/GstAmrnbEnc.prs
%endif

%if %{build_amrwbdec}
%package -n %{bname}-amrwbdec
Summary:	GStreamer plug-in for AMR-WB decoding support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(opencore-amrwb)

%description -n %{bname}-amrwbdec
Plug-in for decoding AMR-Wb under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-amrwbdec
%{_libdir}/gstreamer-%{api}/libgstamrwbdec.so
%endif

### SIDPLAY ###
%package -n %{bname}-sid
Summary:	GStreamer Sid C64 music plugin
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	sidplay-devel >= 1.36.0

%description -n %{bname}-sid
Plugin for playback of C64 SID format music files

%files -n %{bname}-sid
%{_libdir}/gstreamer-%{api}/libgstsid.so

### A52DEC ###
%package -n %{bname}-a52dec
Summary:	GStreamer VOB decoder plugin
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	a52dec-devel >= 0.7.3

%description -n %{bname}-a52dec
Plugin for decoding of VOB files

%files -n %{bname}-a52dec
%{_libdir}/gstreamer-%{api}/libgsta52dec.so

%package -n %{bname}-mpeg
Summary:	GStreamer plug-ins for MPEG video playback and encoding
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libmpeg2)

%description -n %{bname}-mpeg
Plug-ins for playing and encoding MPEG video.

%files -n %{bname}-mpeg
%{_libdir}/gstreamer-%{api}/libgstmpeg2dec.so

%package -n %{bname}-cdio
Summary:	GStreamer plug-in for audio CD playback
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libcdio)
Conflicts:	%{bname}-plugins-good < 0.10.10

%description -n %{bname}-cdio
Plug-in for audio CD playback.

%files -n %{bname}-cdio
%{_libdir}/gstreamer-%{api}/libgstcdio.so

%package -n %{bname}-twolame
Summary:	GStreamer plug-in for MP2 encoding support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(twolame)

%description -n %{bname}-twolame
Plug-in for encoding MP2 under GStreamer.

%files -n %{bname}-twolame
%{_libdir}/gstreamer-%{api}/libgsttwolame.so

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1
autoconf

%build
%configure2_5x \
	--with-package-name='%{distribution} %{name} package' \
	--with-package-origin='%{disturl}' \
%if ! %{build_lame}
	--disable-lame \
%endif
%if %{build_experimental}
	--enable-experimental
%endif

%make

%check
cd tests/check
make check

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-%{api}/libgstasf.so
%{_libdir}/gstreamer-%{api}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{api}/libgstdvdread.so
%{_libdir}/gstreamer-%{api}/libgstdvdsub.so
%{_libdir}/gstreamer-%{api}/libgstiec958.so
%{_libdir}/gstreamer-%{api}/libgstmad.so
%{_libdir}/gstreamer-%{api}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{api}/libgstmpegstream.so
%{_libdir}/gstreamer-%{api}/libgstrmdemux.so
%if %{build_experimental}
%{_libdir}/gstreamer-%{api}/libgstsynaesthesia.so
%endif

