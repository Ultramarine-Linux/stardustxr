rpm.global("commit", gh_commit("stardustxr/flatland")); // TODO: use dev branch
if rpm.changed() {
  rpm.global("commit_date", date());
  rpm.release();
}
