%define tarname	TaskCoach
%define name	taskcoach
%define version 1.3.1
%define release %mkrel 1

Summary:	Your friendly task manager
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/%{tarname}/%{tarname}-%{version}.tar.gz
Patch0:		mandriva.patch
License:	GPLv3+
Group:		Development/Other
Url:		http://www.taskcoach.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.6, wxPythonGTK >= 2.8.9.2
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
%patch0 -p0

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -si s,taskcoach.py,taskcoach, FILE_LIST
mv %{buildroot}%{_bindir}/taskcoach.py %{buildroot}%{_bindir}/taskcoach

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGES.txt COPYRIGHT.txt HACKING.txt LICENSE.txt PUBLICITY.txt README.txt

