%define _glib2 2.2
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
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
%define build_plf 0
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

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-ugly
Version:	0.10.19
Release:	1%{?extrarelsuffix}
License:	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source:		http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
Patch0:		gstreamer-plugins-ugly-0.10.17-amr-linking.patch
Patch1:		gst-plugins-ugly-0.10.19-opencore.patch
#gw for the pixbuf plugin
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel >= %{_glib2}
BuildRequires:	liborc-devel >= 0.4.5
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10.36
BuildRequires:	mesaglu-devel
BuildRequires:	libmad-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libdvdread-devel
%ifnarch %{mips} %{arm}
BuildRequires:	valgrind
%endif
BuildRequires:	libcheck-devel
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
BuildRequires:	liblame-devel >= 3.89

%description -n %{bname}-lame
Plug-in for encoding mp3 with lame under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-lame
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so
%{_datadir}/gstreamer-%{majorminor}/presets/GstX264Enc.prs
%endif

%if %{build_amrnb}
%package -n %{bname}-amrnb
Summary:	GStreamer plug-in for AMR-NB support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	opencore-amr-devel

%description -n %{bname}-amrnb
Plug-in for decoding AMR-NB under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-amrnb
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%{_datadir}/gstreamer-%{majorminor}/presets/GstAmrnbEnc.prs
%endif

%if %{build_amrwbdec}
%package -n %{bname}-amrwbdec
Summary:	GStreamer plug-in for AMR-WB decoding support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	opencore-amr-devel

%description -n %{bname}-amrwbdec
Plug-in for decoding AMR-Wb under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-amrwbdec
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbdec.so
%endif

### SIDPLAY ###
%package -n %{bname}-sid
Summary:	GStreamer Sid C64 music plugin
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	sidplay-devel => 1.36.0

%description -n %{bname}-sid
Plugin for playback of C64 SID format music files

%files -n %{bname}-sid
%{_libdir}/gstreamer-%{majorminor}/libgstsid.so

### A52DEC ###
%package -n %{bname}-a52dec
Summary:	GStreamer VOB decoder plugin
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	a52dec-devel >= 0.7.3

%description -n %{bname}-a52dec
Plugin for decoding of VOB files

%files -n %{bname}-a52dec
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so

%package -n %{bname}-mpeg
Summary:	GStreamer plug-ins for MPEG video playback and encoding
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	libmpeg2dec-devel => 0.3.1

%description -n %{bname}-mpeg
Plug-ins for playing and encoding MPEG video.

%files -n %{bname}-mpeg
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so

%package -n %{bname}-cdio
Summary:	GStreamer plug-in for audio CD playback
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	libcdio-devel
Conflicts:	%{bname}-plugins-good < 0.10.10

%description -n %{bname}-cdio
Plug-in for audio CD playback.

%files -n %{bname}-cdio
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so

%package -n %{bname}-twolame
Summary:	GStreamer plug-in for MP2 encoding support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	libtwolame-devel

%description -n %{bname}-twolame
Plug-in for encoding MP2 under GStreamer.

%files -n %{bname}-twolame
%{_libdir}/gstreamer-%{majorminor}/libgsttwolame.so

%prep
%setup -q -n gst-plugins-ugly-%{version}
%apply_patches
autoconf

%build
%configure2_5x --disable-dependency-tracking \
  --with-package-name='ROSA %{name} package' \
  --with-package-origin='http://www.rosalab.com/' \
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
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang gst-plugins-ugly-%{majorminor}

# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files -f gst-plugins-ugly-%{majorminor}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so
%{_libdir}/gstreamer-%{majorminor}/libgstiec958.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegstream.so
%{_libdir}/gstreamer-%{majorminor}/libgstrmdemux.so
%if %{build_experimental}
%{_libdir}/gstreamer-%{majorminor}/libgstsynaesthesia.so
%endif

%changelog
* Sat Jun 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.10.19-1
- Update to 0.10.19
- Add patch 1 to fix build against new opencore-amr (for restricted build)
- Spec cosmetics

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.10.18-1mdv2011.0
+ Revision: 673414
- new version 0.10.18

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.17-4
+ Revision: 664939
- mass rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.10.17-3
+ Revision: 640311
- rebuild to obsolete old packages

* Mon Feb 21 2011 Götz Waschk <waschk@mandriva.org> 0.10.17-2
+ Revision: 639086
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.17-1
+ Revision: 632308
- new version
- rediff patch

* Mon Dec 06 2010 Götz Waschk <waschk@mandriva.org> 0.10.16-3mdv2011.0
+ Revision: 612073
- rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.16-2mdv2011.0
+ Revision: 593557
- rebuild for gstreamer provides

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2011.0
+ Revision: 575666
- new version
- replace dep on liboil by dep on orc

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.10.15-1mdv2011.0
+ Revision: 550261
- new version
- drop patches 1-5

* Wed May 05 2010 Götz Waschk <waschk@mandriva.org> 0.10.14-4mdv2010.1
+ Revision: 542408
- rebuild again
- add x264 patches

* Wed May 05 2010 Götz Waschk <waschk@mandriva.org> 0.10.14-2mdv2010.1
+ Revision: 542325
- rebuild

* Sun Mar 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2010.1
+ Revision: 515549
- new version
- drop patch 1

* Sat Jan 23 2010 Götz Waschk <waschk@mandriva.org> 0.10.13-6mdv2010.1
+ Revision: 495206
- rebuild

* Thu Dec 10 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-5mdv2010.1
+ Revision: 475970
- rebuild

* Mon Nov 09 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-4mdv2010.1
+ Revision: 463508
- fix build with new x264

* Mon Nov 09 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-3mdv2010.1
+ Revision: 463439
- rebuild for new libcdio

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-2mdv2010.1
+ Revision: 461033
- new version
- support building the amrwbdec element
- drop patch 0
- fix opencore-amr linking

* Wed Oct 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-6mdv2010.0
+ Revision: 458503
- fix mp3 seeking (bug #54729)

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 0.10.12-5mdv2010.0
+ Revision: 448999
- disable valgrind on mips & arm (from Arnaud Patard)

* Thu Jun 18 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-4mdv2010.0
+ Revision: 386944
- move x264 plugin here
- new version

* Sat Mar 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.11-1mdv2009.1
+ Revision: 359791
- new version
- move twolame plugin here

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 0.10.10-1mdv2009.1
+ Revision: 309909
- new version
- drop patch
- reenable checks

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.10.9-2mdv2009.1
+ Revision: 304445
- Add patch from upstream cvs fixing seeking in wmv files
  (bug #45825)

* Wed Oct 29 2008 Götz Waschk <waschk@mandriva.org> 0.10.9-1mdv2009.1
+ Revision: 298226
- disable checks

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.10.9-1mdv2009.0
+ Revision: 278401
- new version
- drop patches
- move cdio plugin here

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-6mdv2009.0
+ Revision: 278253
- rebuild for new libdvdread

* Thu Aug 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.8-5mdv2009.0
+ Revision: 266435
- Patch1: ensure translations are encoded in UTF-8 (GNOME bug #546822)

  + Götz Waschk <waschk@mandriva.org>
    - add experimental build option

* Tue Jul 29 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-4mdv2009.0
+ Revision: 253404
- update the patch from cvs

* Tue Jul 29 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-3mdv2009.0
+ Revision: 252460
- patch for lame plugin (b.g.o #498004)
- remove lame workaround
- fix conditional

* Sat May 24 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-2mdv2009.0
+ Revision: 211033
- disable --as-needed for PLF builds to fix the lame configure check

* Fri May 23 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2009.0
+ Revision: 210258
- new version
- drop patch

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-4mdv2008.1
+ Revision: 187415
- rebuild

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-3mdv2008.1
+ Revision: 187342
- add Mandriva branding

* Wed Feb 27 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-2mdv2008.1
+ Revision: 175749
- fix broken Xing VBR header

* Thu Feb 21 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2008.1
+ Revision: 173580
- new version
- drop patch

* Fri Jan 18 2008 Götz Waschk <waschk@mandriva.org> 0.10.6-2mdv2008.1
+ Revision: 154547
- update mpeg audio parser from CVS
- add missing make call

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jun 20 2007 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2008.0
+ Revision: 41839
- new version


* Thu Dec 14 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2007.0
+ Revision: 96989
- new version

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-3mdv2007.1
+ Revision: 92237
- add optional support for amrnb

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-2mdv2007.1
+ Revision: 92192
- Import gstreamer0.10-plugins-ugly

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-2mdv2007.1
- enable checks

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.0
- New release 0.10.4

* Sun Jun 18 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-2mdv2007.0
- fix buildrequires

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- update file list
- New release 0.10.3

* Thu Feb 23 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.10.2-2mdk
- add BuildRequires: libdvdread-devel

* Wed Feb 22 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- update file list
- New release 0.10.2

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- New release 0.10.1

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-2mdk
- fix buildrequires
- improve description

* Tue Dec 06 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdk
- initial package

