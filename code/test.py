#!/usr/bin/env python3

# info:
# https://github.com/PyGithub/PyGithub

# dependency management with poetry
# https://python-poetry.org/docs/basic-usage/
# https://pygithub.readthedocs.io/en/latest/examples/Repository.html
# cd app-folder
# poetry init
# poetry add package
# poetry install # to install dependencies
# poetry shell # to activate
# exit # to deactivate

# [ 0] github
# [ 1] github42
# [ 2] github2
# [ 3] github-delete
# [ 4] github-create
# [ 5] github-repos
# [ 6] github-cli
# [ 7] github2pypi
# [ 8] github-remote
# [ 9] github-actions

from github import Github
import sys


def move_repo_to_translation_step(repo): # @todo: no return?
		
	# then add translators team
	translators_team.add_to_repos(repo)
	
	# finally set push permissions #@ if repo in write_repos
	translators_team.update_team_repository(repo, "push")


def move_repo_to_revision_step(repo): # @todo: no return?
	
	# first remove translators team
	translators_team.remove_from_repos(repo)
	
	# then add revisers team
	revisers_team.add_to_repos(repo)
	
	# finally set push permissions #@ if repo in write_repos
	revisers_team.update_team_repository(repo, "push")


# First create a Github instance:

# using an access token
# with all perms 
g = Github("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") # @todo: put in text file or env variable

# Github Enterprise with custom hostname
# g = Github(base_url="https://github.com/capstanlqc-ysc/api/v3", login_or_token="access_token")

# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    pass # print(repo.name)
# print(repo.url)

#for repo in g.get_user().get_repos():
    # print(repo.url)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))

org_name = "capstanlqc-ysc"
repo_name = "ysc_es-ES_omt"
# repo = g.get_repo("capstanlqc-ysc/ysc_es-ES_omt")
repo = g.get_repo(f"{org_name}/{repo_name}")

read_repos = [
	"capstanlqc-ysc/source_files", 
	"capstanlqc-ysc/ysc_assets", 
	"capstanlqc-ysc/ysc_settings"
	]

write_repos = [
	"capstanlqc-ysc/ysc_es-MX_omt", 
	"capstanlqc-ysc/ysc_fr-FR_omt", 
	"capstanlqc-ysc/ysc_pl-PL_omt", 
	"capstanlqc-ysc/ysc_ro-RO_omt", 
	"capstanlqc-ysc/ysc_de-DE_omt", 
	"capstanlqc-ysc/ysc_es-ES_omt", 
	"capstanlqc-ysc/ysc_en-GB_omt", 
	"capstanlqc-ysc/target_files"
	]

org = g.get_organization(org_name)
org_teams = org.get_teams()
for team in org_teams: 
	print(team)
	# print(team.get_repos())

# Team(name="revisers", id=7177331)
# Team(name="translators", id=6509223)

translators_team = org.get_team(6509223) # translators
revisers_team = org.get_team(7177331) # revisers

# move_repo_to_translation_step(repo) 

#z = revisers_team.remove_from_repos(repo)
#print(z)


# y = translators_team.add_to_repos(repo)
# print(y) # bool
# x = translators_team.update_team_repository(repo, "push")
# print(x) # None

reposs = g.get_organization(org_name).get_repos()
# for repo in reposs:
# 	print(repo.full_name)
# 	print(translators_team.get_repo_permission(repo))
# 	print(revisers_team.get_repo_permission(repo))
	
# 	if repo.full_name in write_repos:
# 		y = translators_team.add_to_repos(repo)
# 		print(y) # bool
# 		translators_team.update_team_repository(repo, "push")
# 		print(translators_team.get_repo_permission(repo))
# 		print(revisers_team.get_repo_permission(repo))

xlat_team_repos = translators_team.get_repos()
for repo in xlat_team_repos:
	print(repo.full_name)

sys.exit()

print(repo.get_topics())
contents = repo.get_contents("")
# contents = repo.get_contents("README.md")
for content_file in contents:
	print(content_file)


# curl -v -H "Authorization: token TOKEN" https://api.github.com/repos/OWNER/REPO/collaborators/COLLABORATOR -X PUT -d '{"permission":"pull"}'	


print(repo.get_collaborators().reversed[0])
print(repo.get_teams())

repo_teams = repo.get_teams()
# repo = g.get_organization(org_name).get_repo(repo_name)

print(translators_team.name)
print(translators_team.get_repos())
xlat_team_repos = translators_team.get_repos()
for repo in xlat_team_repos:
	print(repo.full_name)

# print(translators_team.has_in_repos(repo=f"{org_name}/{repo_name}"))

# translators_team.add_to_repos("target_files")
tgt_repo = g.get_repo("capstanlqc-ysc/target_files")
repo = g.get_repo("capstanlqc-ysc/ysc_es-ES_omt")
# y = translators_team.add_to_repos(tgt_repo)
# print(y) # bool
# x = translators_team.update_team_repository(tgt_repo, "push")
# print(x) # None
# z = translators_team.remove_from_repos(tgt_repo)
# print(z)

print("---")
xlat_team_repos = translators_team.get_repos()
for repo in xlat_team_repos:
	print(repo.full_name)

print(translators_team.get_repo_permission(repo))
print(revisers_team.get_repo_permission(repo))

rev_team_repos = revisers_team.get_repos()
for repo in rev_team_repos:
	print(repo.full_name)

# has_in_collaborators
# add_to_collaborators
# remove_from_collaborators

# add_to_repos(repo)
# set_repo_permission -> update_team_repository
# get_repos()
# has_in_repos
# remove_from_repos


