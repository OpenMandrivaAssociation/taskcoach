%define tarname	TaskCoach

Summary:	Your friendly task manager
Name:		taskcoach
Version:	1.4.3
Release:	1
Source0:	http://downloads.sourceforge.net/%{name}/%{tarname}-%{version}.tar.gz
Patch1:		taskcoach_gtk3_v3.patch
License:	GPLv3+
Group:		Development/Other
Url:		http://www.taskcoach.org/
BuildRequires: python2
BuildRequires: pythonegg(setuptools)
Requires:	python2
Requires:	wxPythonGTK >= 2.8.9.2
BuildArch:	noarch

%description
Task Coach is a simple open source todo manager to keep track of
personal tasks and todo lists. It grew out of a frustration th at most
task managers do not provide facilities for composite tasks. Often,
tasks and other things todo consist of several activities. Task Coach
is designed to deal with composite tasks. In addition, it offers
effort tracking, categories, and notes. 

%prep
%setup -q -n %{tarname}-%{version}
%apply_patches
%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
rm -rf %{buildroot}%{py2_puresitedir}/buildlib*

%files
%doc CHANGES.txt COPYRIGHT.txt HACKING.txt LICENSE.txt PUBLICITY.txt README.txt
%_bindir/taskcoach.py
%py2_puresitedir/TaskCoach*
%py2_puresitedir/taskcoach*
