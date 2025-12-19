# Changelog

## 0.0.2 (2025-12-19)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/dhurtado14/testforMike/compare/v0.0.1...v0.0.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([9b31e48](https://github.com/dhurtado14/testforMike/commit/9b31e48333275fe31c428be36cf07cb8deea0d3d))
* compat with Python 3.14 ([198ab05](https://github.com/dhurtado14/testforMike/commit/198ab0557280bf50080f5cdb7513f9ef783dedce))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([7ebbdae](https://github.com/dhurtado14/testforMike/commit/7ebbdae6091cdf6bc4c5b47471dfa5655e470a49))
* ensure streams are always closed ([3e4f552](https://github.com/dhurtado14/testforMike/commit/3e4f552c940e6a9e1a98a454e0f9675ffedcfc93))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([0cade29](https://github.com/dhurtado14/testforMike/commit/0cade29948acf8148243af7727b4f9f70a1f9fb8))
* use async_to_httpx_files in patch method ([872d1a7](https://github.com/dhurtado14/testforMike/commit/872d1a7180e67f2e56a4078b9fe48d8072471bba))


### Chores

* add missing docstrings ([26260fd](https://github.com/dhurtado14/testforMike/commit/26260fd937544955697aa8473f0243056ecf41f1))
* add Python 3.14 classifier and testing ([6f4f026](https://github.com/dhurtado14/testforMike/commit/6f4f026942039d63be6d0f05d0896588a2cd34d2))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([86b1771](https://github.com/dhurtado14/testforMike/commit/86b1771efd45c28333ee59bcbf10595c39800460))
* **internal/tests:** avoid race condition with implicit client cleanup ([30ababd](https://github.com/dhurtado14/testforMike/commit/30ababd83bfdc5812e57e0a64d9eb5bc5f1a6d8b))
* **internal:** add `--fix` argument to lint script ([2f3a73b](https://github.com/dhurtado14/testforMike/commit/2f3a73b317d06c1b249e9f584ff550edadd33302))
* **internal:** add missing files argument to base client ([7ed6f83](https://github.com/dhurtado14/testforMike/commit/7ed6f83e74793cc4a1acd647fe34accb1cc911a5))
* **internal:** grammar fix (it's -&gt; its) ([e9b2394](https://github.com/dhurtado14/testforMike/commit/e9b2394fe639e511193c3b2de3cae8d8724ab60f))
* **package:** drop Python 3.8 support ([b8d168c](https://github.com/dhurtado14/testforMike/commit/b8d168c9d677da076ce9493c4ddf7c3b6b71a359))
* speedup initial import ([be5c132](https://github.com/dhurtado14/testforMike/commit/be5c13251e972c69cb60ccd7aeac22e85b52dee9))
* update lockfile ([43e467d](https://github.com/dhurtado14/testforMike/commit/43e467dba9a9976fcb0d069bebaed99e212a7e0b))
* update SDK settings ([a3518f1](https://github.com/dhurtado14/testforMike/commit/a3518f1736ff4420499f746d6c44b617a9f43c93))
