Name:           libdvdnav
Version:        5.0.3
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code

Group:          System Environment/Libraries
License:        GPLv2+
Source0:        https://download.videolan.org/pub/videolan/libdvdnav/%{version}/libdvdnav-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  doxygen
BuildRequires:  libdvdread-devel >= 5.0.2

%description
libdvdnav provides a simple library for reading DVD video discs.
The code is based on Ogle and used in, among others, the Xine dvdnav plug-in.

%package        devel
Summary:        Development files for libdvdnav
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libdvdread-devel >= 5.0.2
Requires:       pkgconfig

%description    devel
libdvdnav-devel contains the files necessary to build packages that use the
libdvdnav library.

%prep
%setup -q

%build
CFLAGS="%{optflags} -fno-strict-aliasing" ./configure \
 --disable-static \
 --libdir=%{_libdir} \
 --prefix=%{_prefix}

%{__make} %{?_smp_mflags}
pushd doc
doxygen doxy.conf
popd

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libdvdnav.la
rm -rf %{buildroot}%{_datadir}/doc/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README
%{_libdir}/libdvdnav.so.*

%files devel
%defattr(-,root,root,-)
%doc TODO doc/html/*
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav
%{_libdir}/pkgconfig/dvdnav.pc

%changelog
* Wed May 18 2016 Bastien Nocera <bnocera@redhat.com> - 5.0.3-1
- Upgrade to 5.0.3
- Fixes a number of playback bugs
Resolves: #1068814

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.2.0-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.2.0-7
- Mass rebuild 2013-12-27

* Thu Jul 18 2013 Matthias Clasen <mclasen@redhat.com> - 4.2.0-5
- Disable strict aliasing

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Dominik Mierzejewski <rpm[AT]greysector.net> 4.2.0-1
- update to 4.2.0

* Mon Apr 11 2011 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.4-0.3.svn1226
- update to SVN r1226

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-0.2.svn1184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 26 2009 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.4-0.1.svn1184
- fix multilib conflict, based on a patch by Rex Dieter (rhbz#477684)
- update to SVN r1184
- move TODO to devel docs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.3-1
- update to 4.1.3 final

* Sun Aug 31 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.3-0.4.rc1
- update to 4.1.3rc1
- require libdvdread with fixed API

* Fri Jul 25 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.3-0.3
- add missing file to -devel

* Thu Jul 17 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.3-0.2
- update to current SVN
- use new external libdvdread

* Fri Jun 06 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.3-0.1
- update to current SVN (pre-4.1.3)
- macroize
- re-enable parallel make

* Sun Apr 13 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.2-1
- update to 4.1.2
- drop obsolete patches (merged upstream)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.1.1-6
- Autorebuild for GCC 4.3

* Sun Jan 27 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.1-5
- fix missing <inttypes.h> include (bug 428910)

* Sun Jan 06 2008 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.1-4
- make sure -devel requires our version of libdvdread-devel

* Thu Nov 22 2007 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.1-3
- fix build with internal libdvdread

* Wed Nov 21 2007 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.1-2
- use upstream non-autotools buildsystem
- build with external libdvdread for older releases
- fix version.h
- fix soname
- fix lib paths on 64bit

* Thu Nov 01 2007 Dominik Mierzejewski <rpm[AT]greysector.net> 4.1.1-1
- switch to new upstream
- libdvdread comes from here now
- apply dvdread udf-related fixes from upstream SVN

* Sun Aug 19 2007 Dominik Mierzejewski <rpm[AT]greysector.net> 0.1.10-4.20070819
- update to current snapshot
- specfile cleanups

* Thu May 03 2007 Dominik Mierzejewski <rpm[AT]greysector.net> 0.1.10-3.20070503
- update to current snapshot from new upstream
- clean up some specfile cruft
- disable static libs
- drop unnecessary explicit dependency on libdvdread

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0.1.10-2
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Wed Oct 13 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.10-0.lvn.1
- Update to 0.1.10.
- Disable dependency tracking to speed up the build.

* Wed Jun 25 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:0.1.9-0.fdr.2: incorporated bugzilla suggestions, new release

* Thu May 29 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:0.1.9-0.fdr.1: initial RPM release
