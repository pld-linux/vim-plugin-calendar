Summary:	Calendar Plugin for VIM
Name:		vim-plugin-calendar
Version:	1.4
Release:	0.1
License:	GPL
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
This VIM plugin lets you fill your diary in vim.
Calendar data fiels are saved under ~/diary/YYYY/MM/DD.cal.

Customizations possible in ~/.vimrc, please see
%{_vimdatadir}/plugin/calendar.vim for details.

%prep
%setup -q -c -T
install %{SOURCE0} calendar.vim

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
install calendar.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/*
