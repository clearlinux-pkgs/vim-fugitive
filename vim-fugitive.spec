#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vim-fugitive
Version  : 2.5
Release  : 1
URL      : https://github.com/tpope/vim-fugitive/archive/v2.5.tar.gz
Source0  : https://github.com/tpope/vim-fugitive/archive/v2.5.tar.gz
Summary  : Git wrapper so awesome, it should be illegal
Group    : Development/Tools
License  : Vim
Requires: vim-fugitive-data = %{version}-%{release}
Patch1: build.patch

%description
No detailed description available

%package data
Summary: data components for the vim-fugitive package.
Group: Data

%description data
data components for the vim-fugitive package.


%prep
%setup -q -n vim-fugitive-2.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547690136
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1547690136
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vim/vim81/autoload/fugitive.vim
/usr/share/vim/vim81/ftdetect/fugitive.vim
/usr/share/vim/vim81/plugin/fugitive.vim
