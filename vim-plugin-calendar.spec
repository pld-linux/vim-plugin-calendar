Summary:	Vim plugin: calendar window
Summary(pl):	Wtyczka Vima: okno kalendarza
Name:		vim-plugin-calendar
Version:	1.4
Release:	1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://vim.sourceforge.net/scripts/download_script.php?src_id=3599
# Source0-md5:	a8f706d899b35659f0e0d3459401caab
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=52
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This plugin provides a calendar window for vim. To start it, use the
:Calendar command.

You can also use 'diary' command wrapper, packaged with this rpm.

Customizations possible in ~/.vimrc, please see
%{_vimdatadir}/plugin/calendar.vim for details.

%description -l pl
Ta wtyczka udostêpnia okno kalendarza dla vima. Aby je uruchomiæ,
nale¿y u¿yæ polecenia :Calendar .

Mo¿na tak¿e u¿yæ polecenia pow³oki 'diary' umieszczonego w tym
pakiecie.

Wtyczka jest konfigurowalna poprzez ~/.vimrc - szczegó³y w pliku
%{_vimdatadir}/plugin/calendar.vim .

%prep
%setup -q -c -T
install %{SOURCE0} calendar.vim

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_vimdatadir}/plugin}
install calendar.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cat <<'EOF' >> $RPM_BUILD_ROOT%{_bindir}/diary
#!/bin/sh
exec vim +CalendarH
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/diary
%{_vimdatadir}/plugin/*
