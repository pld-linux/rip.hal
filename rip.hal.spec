Summary:	Powerful CD audio ripper for GNOME2
Summary(pl):	Potê¿ny ripper p³yt CD dla GNOME2
Name:		rip.hal
Version:	0.0.2
Release:	0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://rip.hal.pl/%{name}-%{version}.tar.gz
# Source0-md5:	70cb0075c856b9e957b77aa6c17db7df
URL:		http://rip.hal.pl/
Vendor:		Michal Zawalich <michuz@pld.org.pl>
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	intltool
BuildRequires:	lame-libs-devel
BuildRequires:	libghttp-devel
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powerful CD audio ripper for GNOME2.

%description -l pl
Potê¿ny ripper p³yt CD dla GNOME2.

%prep 
%setup -q 

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}
%{_datadir}/applications/*.desktop
