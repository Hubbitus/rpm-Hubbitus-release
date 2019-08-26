Name:		Hubbitus-release
Version:		7
Release:		5
Summary:		Hubbitus Repository Configuration
Summary(ru):	Конфигурация репозитория Hubbitus

Group:		System Environment/Base
License:		GPLv2+
URL:			http://hubbitus.info/wiki/Repository
Source0:		Hubbitus.repo

Requires:		epel-release >= 7

BuildArch:	noarch

%description
Hubbitus repository contain mostly packages what I prepare for importing into
Fedoda and EPEL. Sometimes it may take very long time and packages may be
installed from my repository.
Additionally there present free packages, which can't be part of Fedora by some
legal issues. F.e. dkms-tiacx - I have and use Dlink WiFi adapter on TI acx100
(acx111) chipset, but Fedora don't accept anything kernel-modules.

%description -l ru
Hubbitus репозиторий содержит в основном пакеты, которые я готовлю к импорту
в Fedora и EPEL. Иногда этот процесс может занимать весьма продолжительное
время, тогда они доступны отсюда.
Дополнительно здесь свободные пакеты, по тем или иным причинам включение
которых невозможно. Например dkms-tiacx. Я постоянно использую Dlink WiFi карту
на TI acx100 (acx111) чипсете, но в Федоре запрещены пакеты с модулями ядра.

%prep
%setup -c -T


%build

# Repo
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/Hubbitus.repo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Mon Jan 14 2019 Pavel Alexeev <Pahan@Hubbitus.info> - 7-5
- Remove mirror.

* Tue Jun 02 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 7-4
- Change in repo default url http://hubbitus.info/rpm/epel$releasever/ -> http://rpm.hubbitus.info/epel$releasever/ (https://github.com/Hubbitus/Fedora-packaging/issues/3#issuecomment-107397393)
- Cleanup spec (only Epel7 now basically support).
- Step to use Hubbitus.repo.EL precise source name.

* Wed Mar 25 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 7-3
- Require epel-release instead of centos-release to work also on RHEL.

* Fri Mar 06 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 7-2
- OVH block hosting account. Add http://rpm-mirror.hubbitus.info mirror for repo on digitalocean.com
- Change URL to http://hubbitus.info/wiki/Repository

* Thu Sep 11 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 7-1
- Version 7.0

* Tue Feb 5 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 6-1
- Step to EPEL 6.

* Sat Jul 2 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 5-2
- Replace hubbitus.net.ru to hubbitus.info in repo.

* Thu Sep 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 5-1
- Initial release.