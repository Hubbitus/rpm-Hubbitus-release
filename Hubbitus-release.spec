Name:		Hubbitus-release
Version:		25
Release:		1
Summary:		Hubbitus Repository Configuration
Summary(ru):	Конфигурация репозитория Hubbitus

Group:		System Environment/Base
License:		GPLv2+
URL:			http://hubbitus.info/wiki/Repository
Source0:		Hubbitus.repo

Requires:		fedora-release >= 25

BuildArch:	noarch

%description
Hubbitus repository contains mostly packages what I prepare for importing into
Fedora. Sometimes it may take very long time and packages may be installed from
my repository.
Additionally there present free packages, which can't be part of Fedora by some
legal issues. F.e. dkms-tiacx - I have and use Dlink WiFi adapter on TI acx100
(acx111) chipset, but Fedora don't accept anything kernel-modules.

%description -l ru
Hubbitus репозиторий содержит в основном пакеты, которые я готовлю к импорту
в Fedora. Иногда этот процесс может занимать весьма продолжительное время,
тогда они доступны отсюда.
Дополнительно здесь свободные пакеты, по тем или иным причинам включение
которых невозможно. Например dkms-tiacx. Я постоянно использую Dlink WiFi карту
на TI acx100 (acx111) чипсете, но в Федоре запрещены пакеты с модулями ядра.

%prep
%setup -c -T

%build


%install
# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/Hubbitus.repo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Sat Oct 01 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 25-1
- Split out into separate repository. Use branches instead of files mess.
- Fedora25 build.

* Sat Nov 07 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 23-1
- Update to Fedora 23.

* Fri Mar 06 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 22-3
- OVH block hosting account. Add http://rpm-mirror.hubbitus.info mirror for repo on digitalocean.com
- Change URL to http://hubbitus.info/wiki/Repository

* Fri Oct 24 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 22-2
- Fix repo file.

* Fri Oct 24 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 22-1
- Build for Fedora 22 - rawhide

* Mon Jul 8 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 19-1
- Fedora 19 released!

* Tue Feb 5 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 18-1
- New Fedora release!

* Mon Apr 30 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 17-1
- New 17 release of Fedora (TC2)!

* Sun Oct 2 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 16-1
- Build for Fedora 16 (now Alpha)

* Sat Jul 2 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 15-2
- Replace hubbitus.net.ru to hubbitus.info in repo.

* Thu May 5 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 15-1
- Build for Fedora 15

* Thu Oct 21 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 14-1
- Build for Fedora 14

* Thu Sep 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 11-1
- Initial release.