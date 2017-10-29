





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-d7137690e30123bade38abb082ac79f36cc7a105ff92e602405f53b725465cab.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-7a6d219bc4266e5db3eb55793bd9e9aa29d52d9e430f7493a8cfd1fc3a4f3509.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-9628bfea02884cc06cee3aa24062d81f93e06de09ed5bac5557deb155500e539.css" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>models/README.md at master · tensorflow/models · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars2.githubusercontent.com/u/15658638?s=400&amp;v=4" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="tensorflow/models" property="og:title" /><meta content="https://github.com/tensorflow/models" property="og:url" /><meta content="models - Models built with TensorFlow" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="8038:2CBA4:42423:6CB39:59E359C8" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="8038:2CBA4:42423:6CB39:59E359C8" name="octolytics-dimension-request_id" /><meta content="sea" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="OTgwZTRkMGY4NDlkMTZmZDE3YTcwMTk0NjNiNDZmODBiNjdiNjBlODk5NWQ3ZTQ5MWVhM2M5NDFlNThiOGFhZnx7InJlbW90ZV9hZGRyZXNzIjoiMjE4LjIyNy4yMTEuMTMxIiwicmVxdWVzdF9pZCI6IjgwMzg6MkNCQTQ6NDI0MjM6NkNCMzk6NTlFMzU5QzgiLCJ0aW1lc3RhbXAiOjE1MDgwNzE4ODEsImhvc3QiOiJnaXRodWIuY29tIn0=">


  <meta name="html-safe-nonce" content="2afae4d1164c0cb765fa200eff04c74904699090">

  <meta http-equiv="x-pjax-version" content="9860aabee28c9110d9e3b6caf992fb9c">
  

      <link href="https://github.com/tensorflow/models/commits/master.atom" rel="alternate" title="Recent Commits to models:master" type="application/atom+xml">

  <meta name="description" content="models - Models built with TensorFlow">
  <meta name="go-import" content="github.com/tensorflow/models git https://github.com/tensorflow/models.git">

  <meta content="15658638" name="octolytics-dimension-user_id" /><meta content="tensorflow" name="octolytics-dimension-user_login" /><meta content="51117837" name="octolytics-dimension-repository_id" /><meta content="tensorflow/models" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="51117837" name="octolytics-dimension-repository_network_root_id" /><meta content="tensorflow/models" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/tensorflow/models/blob/master/research/slim/README.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        <header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
      <a class="header-logo-invertocat my-0" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
      </a>

    </div>

    <div class="HeaderMenu HeaderMenu--bright d-flex flex-justify-between flex-auto">
        <nav class="mt-0">
          <ul class="d-flex list-style-none">
              <li class="ml-2">
                <a href="/features" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features/project-management /features/code-review /features/project-management /features/integrations /features">
                  Features
</a>              </li>
              <li class="ml-4">
                <a href="/business" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
                  Business
</a>              </li>

              <li class="ml-4">
                <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                  Explore
</a>              </li>

              <li class="ml-4">
                    <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:marketplace" data-selected-links=" /marketplace">
                      Marketplace
</a>              </li>
              <li class="ml-4">
                <a href="/pricing" class="js-selected-navigation-item HeaderNavlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing/developer /pricing/team /pricing/business-hosted /pricing/business-enterprise /pricing">
                  Pricing
</a>              </li>
          </ul>
        </nav>

      <div class="d-flex">
          <div class="d-lg-flex flex-items-center mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/tensorflow/models/search" class="js-site-search-form" data-scoped-search-url="/tensorflow/models/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/tensorflow/models/blob/master/research/slim/README.md" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

          </div>

        <span class="d-inline-block">
            <div class="HeaderNavlink px-0 py-2 m-0">
              <a class="text-bold text-white no-underline" href="/login?return_to=%2Ftensorflow%2Fmodels%2Fblob%2Fmaster%2Fresearch%2Fslim%2FREADME.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
                <span class="text-gray">or</span>
                <a class="text-bold text-white no-underline" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
            </div>
        </span>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



  



    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav ">
      <div class="repohead-details-container clearfix container ">

        <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Ftensorflow%2Fmodels"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/tensorflow/models/watchers"
     aria-label="1632 users are watching this repository">
    1,632
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Ftensorflow%2Fmodels"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/tensorflow/models/stargazers"
      aria-label="22165 users starred this repository">
      22,165
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Ftensorflow%2Fmodels"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/tensorflow/models/network" class="social-count"
       aria-label="10279 users forked this repository">
      10,279
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/tensorflow" class="url fn" rel="author">tensorflow</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/tensorflow/models" data-pjax="#js-repo-pjax-container">models</a></strong>

</h1>

      </div>
      
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/tensorflow/models" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /tensorflow/models" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/tensorflow/models/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /tensorflow/models/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">360</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/tensorflow/models/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /tensorflow/models/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">121</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/tensorflow/models/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /tensorflow/models/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a href="/tensorflow/models/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /tensorflow/models/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a href="/tensorflow/models/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /tensorflow/models/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/tensorflow/models/blob/baf8deb53bcbf949ffdb85c4f0f0d53c0c6e979d/research/slim/README.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:0ced899ffd918dbc7a143ea76d16ba73 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/models/blob/av8ramit-patch-2/research/slim/README.md"
               data-name="av8ramit-patch-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                av8ramit-patch-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/models/blob/benchmarks/research/slim/README.md"
               data-name="benchmarks"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                benchmarks
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/tensorflow/models/blob/master/research/slim/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/tensorflow/models/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/tensorflow/models"><span>models</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/tensorflow/models/tree/master/research"><span>research</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/tensorflow/models/tree/master/research/slim"><span>slim</span></a></span><span class="separator">/</span><strong class="final-path">README.md</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/tensorflow/models/commit/4a705e08ca8f28bd05bdc2287211ad8aba0bf98a" data-pjax>
          4a705e0
        </a>
        <relative-time datetime="2017-09-23T01:07:22Z">Sep 23, 2017</relative-time>
      </span>
      <div>
        <img alt="@nealwu" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/726075?v=4&amp;s=40" width="20" />
        <a href="/nealwu" class="user-mention" rel="contributor">nealwu</a>
          <a href="/tensorflow/models/commit/4a705e08ca8f28bd05bdc2287211ad8aba0bf98a" class="message" data-pjax="true" title="Fix broken links in the models repo (#2445)">Fix broken links in the models repo (</a><a href="https://github.com/tensorflow/models/pull/2445" class="issue-link js-issue-link" data-error-text="Failed to load issue title" data-id="259970417" data-permission-text="Issue title is private" data-url="https://github.com/tensorflow/models/issues/2445">#2445</a><a href="/tensorflow/models/commit/4a705e08ca8f28bd05bdc2287211ad8aba0bf98a" class="message" data-pjax="true" title="Fix broken links in the models repo (#2445)">)</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>2</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="nealwu" href="/tensorflow/models/commits/4a705e08ca8f28bd05bdc2287211ad8aba0bf98a/research/slim/README.md?author=nealwu"><img alt="@nealwu" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/726075?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="dave-andersen" href="/tensorflow/models/commits/4a705e08ca8f28bd05bdc2287211ad8aba0bf98a/research/slim/README.md?author=dave-andersen"><img alt="@dave-andersen" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/827870?v=4&amp;s=40" width="20" /> </a>


    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@nealwu" height="24" src="https://avatars3.githubusercontent.com/u/726075?v=4&amp;s=48" width="24" />
            <a href="/nealwu">nealwu</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@dave-andersen" height="24" src="https://avatars1.githubusercontent.com/u/827870?v=4&amp;s=48" width="24" />
            <a href="/dave-andersen">dave-andersen</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/tensorflow/models/raw/master/research/slim/README.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/tensorflow/models/blame/master/research/slim/README.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/tensorflow/models/commits/master/research/slim/README.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      513 lines (398 sloc)
      <span class="file-info-divider"></span>
    23.5 KB
  </div>
</div>

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a href="#tensorflow-slim-image-classification-model-library" aria-hidden="true" class="anchor" id="user-content-tensorflow-slim-image-classification-model-library"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>TensorFlow-Slim image classification model library</h1>
<p><a href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim">TF-slim</a>
is a new lightweight high-level API of TensorFlow (<code>tensorflow.contrib.slim</code>)
for defining, training and evaluating complex
models. This directory contains
code for training and evaluating several widely used Convolutional Neural
Network (CNN) image classification models using TF-slim.
It contains scripts that will allow
you to train models from scratch or fine-tune them from pre-trained network
weights. It also contains code for downloading standard image datasets,
converting them
to TensorFlow's native TFRecord format and reading them in using TF-Slim's
data reading and queueing utilities. You can easily train any model on any of
these datasets, as we demonstrate below. We've also included a
<a href="https://github.com/tensorflow/models/blob/master/research/slim/slim_walkthrough.ipynb">jupyter notebook</a>,
which provides working examples of how to use TF-Slim for image classification.
For developing or modifying your own models, see also the <a href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim">main TF-Slim page</a>.</p>
<h2><a href="#contacts" aria-hidden="true" class="anchor" id="user-content-contacts"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Contacts</h2>
<p>Maintainers of TF-slim:</p>
<ul>
<li>Nathan Silberman,
github: <a href="https://github.com/nathansilberman">nathansilberman</a></li>
<li>Sergio Guadarrama, github: <a href="https://github.com/sguada">sguada</a></li>
</ul>
<h2><a href="#table-of-contents" aria-hidden="true" class="anchor" id="user-content-table-of-contents"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Table of contents</h2>
<p><a href="#Install">Installation and setup</a><br>
<a href="#Data">Preparing the datasets</a><br>
<a href="#Pretrained">Using pre-trained models</a><br>
<a href="#Training">Training from scratch</a><br>
<a href="#Tuning">Fine tuning to a new task</a><br>
<a href="#Eval">Evaluating performance</a><br>
<a href="#Export">Exporting Inference Graph</a><br>
<a href="#Troubleshooting">Troubleshooting</a><br></p>
<h1><a href="#installation" aria-hidden="true" class="anchor" id="user-content-installation"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h1>
<p><a id="user-content-Install"></a></p>
<p>In this section, we describe the steps required to install the appropriate
prerequisite packages.</p>
<h2><a href="#installing-latest-version-of-tf-slim" aria-hidden="true" class="anchor" id="user-content-installing-latest-version-of-tf-slim"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installing latest version of TF-slim</h2>
<p>TF-Slim is available as <code>tf.contrib.slim</code> via TensorFlow 1.0. To test that your
installation is working, execute the following command; it should run without
raising any errors.</p>
<pre><code>python -c "import tensorflow.contrib.slim as slim; eval = slim.evaluation.evaluate_once"
</code></pre>
<h2><a href="#installing-the-tf-slim-image-models-library" aria-hidden="true" class="anchor" id="user-content-installing-the-tf-slim-image-models-library"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installing the TF-slim image models library</h2>
<p>To use TF-Slim for image classification, you also have to install
the <a href="https://github.com/tensorflow/models/tree/master/research/slim">TF-Slim image models library</a>,
which is not part of the core TF library.
To do this, check out the
<a href="https://github.com/tensorflow/models/">tensorflow/models</a> repository as follows:</p>
<div class="highlight highlight-source-shell"><pre><span class="pl-c1">cd</span> <span class="pl-smi">$HOME</span>/workspace
git clone https://github.com/tensorflow/models/</pre></div>
<p>This will put the TF-Slim image models library in <code>$HOME/workspace/models/research/slim</code>.
(It will also create a directory called
<a href="https://github.com/tensorflow/models/tree/master/research/inception">models/inception</a>,
which contains an older version of slim; you can safely ignore this.)</p>
<p>To verify that this has worked, execute the following commands; it should run
without raising any errors.</p>
<pre><code>cd $HOME/workspace/models/research/slim
python -c "from nets import cifarnet; mynet = cifarnet.cifarnet"
</code></pre>
<h1><a href="#preparing-the-datasets" aria-hidden="true" class="anchor" id="user-content-preparing-the-datasets"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Preparing the datasets</h1>
<p><a id="user-content-Data"></a></p>
<p>As part of this library, we've included scripts to download several popular
image datasets (listed below) and convert them to slim format.</p>
<table>
<thead>
<tr>
<th align="center">Dataset</th>
<th align="center">Training Set Size</th>
<th align="center">Testing Set Size</th>
<th align="center">Number of Classes</th>
<th align="center">Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Flowers</td>
<td align="center">2500</td>
<td align="center">2500</td>
<td align="center">5</td>
<td align="center">Various sizes (source: Flickr)</td>
</tr>
<tr>
<td align="center"><a href="https://www.cs.toronto.edu/%7Ekriz/cifar.html">Cifar10</a></td>
<td align="center">60k</td>
<td align="center">10k</td>
<td align="center">10</td>
<td align="center">32x32 color</td>
</tr>
<tr>
<td align="center"><a href="http://yann.lecun.com/exdb/mnist/">MNIST</a></td>
<td align="center">60k</td>
<td align="center">10k</td>
<td align="center">10</td>
<td align="center">28x28 gray</td>
</tr>
<tr>
<td align="center"><a href="http://www.image-net.org/challenges/LSVRC/2012/">ImageNet</a></td>
<td align="center">1.2M</td>
<td align="center">50k</td>
<td align="center">1000</td>
<td align="center">Various sizes</td>
</tr></tbody></table>
<h2><a href="#downloading-and-converting-to-tfrecord-format" aria-hidden="true" class="anchor" id="user-content-downloading-and-converting-to-tfrecord-format"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Downloading and converting to TFRecord format</h2>
<p>For each dataset, we'll need to download the raw data and convert it to
TensorFlow's native
<a href="https://www.tensorflow.org/versions/r0.10/api_docs/python/python_io.html#tfrecords-format-details">TFRecord</a>
format. Each TFRecord contains a
<a href="https://github.com/tensorflow/tensorflow/blob/r0.10/tensorflow/core/example/example.proto">TF-Example</a>
protocol buffer. Below we demonstrate how to do this for the Flowers dataset.</p>
<div class="highlight highlight-source-shell"><pre>$ DATA_DIR=/tmp/data/flowers
$ python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir=<span class="pl-s"><span class="pl-pds">"</span><span class="pl-smi">${DATA_DIR}</span><span class="pl-pds">"</span></span></pre></div>
<p>When the script finishes you will find several TFRecord files created:</p>
<div class="highlight highlight-source-shell"><pre>$ ls <span class="pl-smi">${DATA_DIR}</span>
flowers_train-00000-of-00005.tfrecord
...
flowers_train-00004-of-00005.tfrecord
flowers_validation-00000-of-00005.tfrecord
...
flowers_validation-00004-of-00005.tfrecord
labels.txt</pre></div>
<p>These represent the training and validation data, sharded over 5 files each.
You will also find the <code>$DATA_DIR/labels.txt</code> file which contains the mapping
from integer labels to class names.</p>
<p>You can use the same script to create the mnist and cifar10 datasets.
However, for ImageNet, you have to follow the instructions
<a href="https://github.com/tensorflow/models/blob/master/research/inception/README.md#getting-started">here</a>.
Note that you first have to sign up for an account at image-net.org.
Also, the download can take several hours, and could use up to 500GB.</p>
<h2><a href="#creating-a-tf-slim-dataset-descriptor" aria-hidden="true" class="anchor" id="user-content-creating-a-tf-slim-dataset-descriptor"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Creating a TF-Slim Dataset Descriptor.</h2>
<p>Once the TFRecord files have been created, you can easily define a Slim
<a href="https://github.com/tensorflow/tensorflow/blob/r0.10/tensorflow/contrib/slim/python/slim/data/dataset.py">Dataset</a>,
which stores pointers to the data file, as well as various other pieces of
metadata, such as the class labels, the train/test split, and how to parse the
TFExample protos. We have included the TF-Slim Dataset descriptors
for
<a href="https://github.com/tensorflow/models/blob/master/research/slim/datasets/cifar10.py">Cifar10</a>,
<a href="https://github.com/tensorflow/models/blob/master/research/slim/datasets/imagenet.py">ImageNet</a>,
<a href="https://github.com/tensorflow/models/blob/master/research/slim/datasets/flowers.py">Flowers</a>,
and
<a href="https://github.com/tensorflow/models/blob/master/research/slim/datasets/mnist.py">MNIST</a>.
An example of how to load data using a TF-Slim dataset descriptor using a
TF-Slim
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/slim/python/slim/data/dataset_data_provider.py">DatasetDataProvider</a>
is found below:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> tensorflow <span class="pl-k">as</span> tf
<span class="pl-k">from</span> datasets <span class="pl-k">import</span> flowers

slim <span class="pl-k">=</span> tf.contrib.slim

<span class="pl-c"><span class="pl-c">#</span> Selects the 'validation' dataset.</span>
dataset <span class="pl-k">=</span> flowers.get_split(<span class="pl-s"><span class="pl-pds">'</span>validation<span class="pl-pds">'</span></span>, <span class="pl-c1">DATA_DIR</span>)

<span class="pl-c"><span class="pl-c">#</span> Creates a TF-Slim DataProvider which reads the dataset in the background</span>
<span class="pl-c"><span class="pl-c">#</span> during both training and testing.</span>
provider <span class="pl-k">=</span> slim.dataset_data_provider.DatasetDataProvider(dataset)
[image, label] <span class="pl-k">=</span> provider.get([<span class="pl-s"><span class="pl-pds">'</span>image<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>label<span class="pl-pds">'</span></span>])</pre></div>
<h2><a href="#an-automated-script-for-processing-imagenet-data" aria-hidden="true" class="anchor" id="user-content-an-automated-script-for-processing-imagenet-data"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>An automated script for processing ImageNet data.</h2>
<p>Training a model with the ImageNet dataset is a common request. To facilitate
working with the ImageNet dataset, we provide an automated script for
downloading and processing the ImageNet dataset into the native TFRecord
format.</p>
<p>The TFRecord format consists of a set of sharded files where each entry is a serialized <code>tf.Example</code> proto. Each <code>tf.Example</code> proto contains the ImageNet image (JPEG encoded) as well as metadata such as label and bounding box information.</p>
<p>We provide a single <a href="/tensorflow/models/blob/master/research/slim/datasets/download_and_preprocess_imagenet.sh">script</a> for
downloading and converting ImageNet data to TFRecord format. Downloading and
preprocessing the data may take several hours (up to half a day) depending on
your network and computer speed. Please be patient.</p>
<p>To begin, you will need to sign up for an account with [ImageNet]
(<a href="http://image-net.org">http://image-net.org</a>) to gain access to the data. Look for the sign up page,
create an account and request an access key to download the data.</p>
<p>After you have <code>USERNAME</code> and <code>PASSWORD</code>, you are ready to run our script. Make
sure that your hard disk has at least 500 GB of free space for downloading and
storing the data. Here we select <code>DATA_DIR=$HOME/imagenet-data</code> as such a
location but feel free to edit accordingly.</p>
<p>When you run the below script, please enter <em>USERNAME</em> and <em>PASSWORD</em> when
prompted. This will occur at the very beginning. Once these values are entered,
you will not need to interact with the script again.</p>
<div class="highlight highlight-source-shell"><pre><span class="pl-c"><span class="pl-c">#</span> location of where to place the ImageNet data</span>
DATA_DIR=<span class="pl-smi">$HOME</span>/imagenet-data

<span class="pl-c"><span class="pl-c">#</span> build the preprocessing script.</span>
bazel build slim/download_and_preprocess_imagenet

<span class="pl-c"><span class="pl-c">#</span> run it</span>
bazel-bin/slim/download_and_preprocess_imagenet <span class="pl-s"><span class="pl-pds">"</span><span class="pl-smi">${DATA_DIR}</span><span class="pl-pds">"</span></span></pre></div>
<p>The final line of the output script should read:</p>
<div class="highlight highlight-source-shell"><pre>2016-02-17 14:30:17.287989: Finished writing all 1281167 images <span class="pl-k">in</span> data set.</pre></div>
<p>When the script finishes you will find 1024 and 128 training and validation
files in the <code>DATA_DIR</code>. The files will match the patterns <code>train-????-of-1024</code>
and <code>validation-?????-of-00128</code>, respectively.</p>
<p><a href="https://www.youtube.com/watch?v=9bZkp7q19f0">Congratulations!</a> You are now
ready to train or evaluate with the ImageNet data set.</p>
<h1><a href="#pre-trained-models" aria-hidden="true" class="anchor" id="user-content-pre-trained-models"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Pre-trained Models</h1>
<p><a id="user-content-Pretrained"></a></p>
<p>Neural nets work best when they have many parameters, making them powerful
function approximators.
However, this  means they must be trained on very large datasets. Because
training models from scratch can be a very computationally intensive process
requiring days or even weeks, we provide various pre-trained models,
as listed below. These CNNs have been trained on the
<a href="http://www.image-net.org/challenges/LSVRC/2012/">ILSVRC-2012-CLS</a>
image classification dataset.</p>
<p>In the table below, we list each model, the corresponding
TensorFlow model file, the link to the model checkpoint, and the top 1 and top 5
accuracy (on the imagenet test set).
Note that the VGG and ResNet V1 parameters have been converted from their original
caffe formats
(<a href="https://github.com/BVLC/caffe/wiki/Model-Zoo#models-used-by-the-vgg-team-in-ilsvrc-2014">here</a>
and
<a href="https://github.com/KaimingHe/deep-residual-networks">here</a>),
whereas the Inception and ResNet V2 parameters have been trained internally at
Google. Also be aware that these accuracies were computed by evaluating using a
single image crop. Some academic papers report higher accuracy by using multiple
crops at multiple scales.</p>
<table>
<thead>
<tr>
<th align="center">Model</th>
<th align="center">TF-Slim File</th>
<th align="center">Checkpoint</th>
<th align="center">Top-1 Accuracy</th>
<th align="center">Top-5 Accuracy</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1409.4842v1">Inception V1</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/inception_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/inception_v1_2016_08_28.tar.gz">inception_v1_2016_08_28.tar.gz</a></td>
<td align="center">69.8</td>
<td align="center">89.6</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1502.03167">Inception V2</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/inception_v2.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/inception_v2_2016_08_28.tar.gz">inception_v2_2016_08_28.tar.gz</a></td>
<td align="center">73.9</td>
<td align="center">91.8</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1512.00567">Inception V3</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/inception_v3.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz">inception_v3_2016_08_28.tar.gz</a></td>
<td align="center">78.0</td>
<td align="center">93.9</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1602.07261">Inception V4</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/inception_v4.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/inception_v4_2016_09_09.tar.gz">inception_v4_2016_09_09.tar.gz</a></td>
<td align="center">80.2</td>
<td align="center">95.2</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1602.07261">Inception-ResNet-v2</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/inception_resnet_v2.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/inception_resnet_v2_2016_08_30.tar.gz">inception_resnet_v2_2016_08_30.tar.gz</a></td>
<td align="center">80.4</td>
<td align="center">95.3</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1512.03385">ResNet V1 50</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz">resnet_v1_50_2016_08_28.tar.gz</a></td>
<td align="center">75.2</td>
<td align="center">92.2</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1512.03385">ResNet V1 101</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz">resnet_v1_101_2016_08_28.tar.gz</a></td>
<td align="center">76.4</td>
<td align="center">92.9</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1512.03385">ResNet V1 152</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v1_152_2016_08_28.tar.gz">resnet_v1_152_2016_08_28.tar.gz</a></td>
<td align="center">76.8</td>
<td align="center">93.2</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1603.05027">ResNet V2 50</a>^</td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v2.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v2_50_2017_04_14.tar.gz">resnet_v2_50_2017_04_14.tar.gz</a></td>
<td align="center">75.6</td>
<td align="center">92.8</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1603.05027">ResNet V2 101</a>^</td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v2.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v2_101_2017_04_14.tar.gz">resnet_v2_101_2017_04_14.tar.gz</a></td>
<td align="center">77.0</td>
<td align="center">93.7</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1603.05027">ResNet V2 152</a>^</td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v2.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/resnet_v2_152_2017_04_14.tar.gz">resnet_v2_152_2017_04_14.tar.gz</a></td>
<td align="center">77.8</td>
<td align="center">94.1</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/abs/1603.05027">ResNet V2 200</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/resnet_v2.py">Code</a></td>
<td align="center"><a href="/tensorflow/models/blob/master/research/slim">TBA</a></td>
<td align="center">79.9*</td>
<td align="center">95.2*</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1409.1556.pdf">VGG 16</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/vgg.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz">vgg_16_2016_08_28.tar.gz</a></td>
<td align="center">71.5</td>
<td align="center">89.8</td>
</tr>
<tr>
<td align="center"><a href="http://arxiv.org/abs/1409.1556.pdf">VGG 19</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/vgg.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/vgg_19_2016_08_28.tar.gz">vgg_19_2016_08_28.tar.gz</a></td>
<td align="center">71.1</td>
<td align="center">89.8</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/pdf/1704.04861.pdf">MobileNet_v1_1.0_224</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/mobilenet_v1_1.0_224_2017_06_14.tar.gz">mobilenet_v1_1.0_224_2017_06_14.tar.gz</a></td>
<td align="center">70.7</td>
<td align="center">89.5</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/pdf/1704.04861.pdf">MobileNet_v1_0.50_160</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/mobilenet_v1_0.50_160_2017_06_14.tar.gz">mobilenet_v1_0.50_160_2017_06_14.tar.gz</a></td>
<td align="center">59.9</td>
<td align="center">82.5</td>
</tr>
<tr>
<td align="center"><a href="https://arxiv.org/pdf/1704.04861.pdf">MobileNet_v1_0.25_128</a></td>
<td align="center"><a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.py">Code</a></td>
<td align="center"><a href="http://download.tensorflow.org/models/mobilenet_v1_0.25_128_2017_06_14.tar.gz">mobilenet_v1_0.25_128_2017_06_14.tar.gz</a></td>
<td align="center">41.3</td>
<td align="center">66.2</td>
</tr></tbody></table>
<p>^ ResNet V2 models use Inception pre-processing and input image size of 299 (use
<code>--preprocessing_name inception --eval_image_size 299</code> when using
<code>eval_image_classifier.py</code>). Performance numbers for ResNet V2 models are
reported on the ImageNet validation set.</p>
<p>All 16 MobileNet Models reported in the <a href="https://arxiv.org/abs/1704.04861">MobileNet Paper</a> can be found <a href="https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet_v1.md">here</a>.</p>
<p>(*): Results quoted from the <a href="https://arxiv.org/abs/1603.05027">paper</a>.</p>
<p>Here is an example of how to download the Inception V3 checkpoint:</p>
<div class="highlight highlight-source-shell"><pre>$ CHECKPOINT_DIR=/tmp/checkpoints
$ mkdir <span class="pl-smi">${CHECKPOINT_DIR}</span>
$ wget http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz
$ tar -xvf inception_v3_2016_08_28.tar.gz
$ mv inception_v3.ckpt <span class="pl-smi">${CHECKPOINT_DIR}</span>
$ rm inception_v3_2016_08_28.tar.gz</pre></div>
<h1><a href="#training-a-model-from-scratch" aria-hidden="true" class="anchor" id="user-content-training-a-model-from-scratch"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Training a model from scratch.</h1>
<p><a id="user-content-Training"></a></p>
<p>We provide an easy way to train a model from scratch using any TF-Slim dataset.
The following example demonstrates how to train Inception V3 using the default
parameters on the ImageNet dataset.</p>
<div class="highlight highlight-source-shell"><pre>DATASET_DIR=/tmp/imagenet
TRAIN_DIR=/tmp/train_logs
python train_image_classifier.py \
    --train_dir=<span class="pl-smi">${TRAIN_DIR}</span> \
    --dataset_name=imagenet \
    --dataset_split_name=train \
    --dataset_dir=<span class="pl-smi">${DATASET_DIR}</span> \
    --model_name=inception_v3</pre></div>
<p>This process may take several days, depending on your hardware setup.
For convenience, we provide a way to train a model on multiple GPUs,
and/or multiple CPUs, either synchrononously or asynchronously.
See <a href="https://github.com/tensorflow/models/blob/master/research/slim/deployment/model_deploy.py">model_deploy</a>
for details.</p>
<h3><a href="#tensorboard" aria-hidden="true" class="anchor" id="user-content-tensorboard"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>TensorBoard</h3>
<p>To visualize the losses and other metrics during training, you can use
<a href="https://github.com/tensorflow/tensorboard">TensorBoard</a>
by running the command below.</p>
<div class="highlight highlight-source-shell"><pre>tensorboard --logdir=<span class="pl-smi">${TRAIN_DIR}</span></pre></div>
<p>Once TensorBoard is running, navigate your web browser to <a href="http://localhost:6006">http://localhost:6006</a>.</p>
<h1><a href="#fine-tuning-a-model-from-an-existing-checkpoint" aria-hidden="true" class="anchor" id="user-content-fine-tuning-a-model-from-an-existing-checkpoint"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Fine-tuning a model from an existing checkpoint</h1>
<p><a id="user-content-Tuning"></a></p>
<p>Rather than training from scratch, we'll often want to start from a pre-trained
model and fine-tune it.
To indicate a checkpoint from which to fine-tune, we'll call training with
the <code>--checkpoint_path</code> flag and assign it an absolute path to a checkpoint
file.</p>
<p>When fine-tuning a model, we need to be careful about restoring checkpoint
weights. In particular, when we fine-tune a model on a new task with a different
number of output labels, we wont be able restore the final logits (classifier)
layer. For this, we'll use the <code>--checkpoint_exclude_scopes</code> flag. This flag
hinders certain variables from being loaded. When fine-tuning on a
classification task using a different number of classes than the trained model,
the new model will have a final 'logits' layer whose dimensions differ from the
pre-trained model. For example, if fine-tuning an ImageNet-trained model on
Flowers, the pre-trained logits layer will have dimensions <code>[2048 x 1001]</code> but
our new logits layer will have dimensions <code>[2048 x 5]</code>. Consequently, this
flag indicates to TF-Slim to avoid loading these weights from the checkpoint.</p>
<p>Keep in mind that warm-starting from a checkpoint affects the model's weights
only during the initialization of the model. Once a model has started training,
a new checkpoint will be created in <code>${TRAIN_DIR}</code>. If the fine-tuning
training is stopped and restarted, this new checkpoint will be the one from
which weights are restored and not the <code>${checkpoint_path}$</code>. Consequently,
the flags <code>--checkpoint_path</code> and <code>--checkpoint_exclude_scopes</code> are only used
during the <code>0-</code>th global step (model initialization). Typically for fine-tuning
one only want train a sub-set of layers, so the flag <code>--trainable_scopes</code> allows
to specify which subsets of layers should trained, the rest would remain frozen.</p>
<p>Below we give an example of
<a href="https://github.com/tensorflow/models/blob/master/research/slim/scripts/finetune_inception_v3_on_flowers.sh">fine-tuning inception-v3 on flowers</a>,
inception_v3  was trained on ImageNet with 1000 class labels, but the flowers
dataset only have 5 classes. Since the dataset is quite small we will only train
the new layers.</p>
<div class="highlight highlight-source-shell"><pre>$ DATASET_DIR=/tmp/flowers
$ TRAIN_DIR=/tmp/flowers-models/inception_v3
$ CHECKPOINT_PATH=/tmp/my_checkpoints/inception_v3.ckpt
$ python train_image_classifier.py \
    --train_dir=<span class="pl-smi">${TRAIN_DIR}</span> \
    --dataset_dir=<span class="pl-smi">${DATASET_DIR}</span> \
    --dataset_name=flowers \
    --dataset_split_name=train \
    --model_name=inception_v3 \
    --checkpoint_path=<span class="pl-smi">${CHECKPOINT_PATH}</span> \
    --checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits \
    --trainable_scopes=InceptionV3/Logits,InceptionV3/AuxLogits</pre></div>
<h1><a href="#evaluating-performance-of-a-model" aria-hidden="true" class="anchor" id="user-content-evaluating-performance-of-a-model"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Evaluating performance of a model</h1>
<p><a id="user-content-Eval"></a></p>
<p>To evaluate the performance of a model (whether pretrained or your own),
you can use the eval_image_classifier.py script, as shown below.</p>
<p>Below we give an example of downloading the pretrained inception model and
evaluating it on the imagenet dataset.</p>
<div class="highlight highlight-source-shell"><pre>CHECKPOINT_FILE = <span class="pl-smi">${CHECKPOINT_DIR}</span>/inception_v3.ckpt  <span class="pl-c"><span class="pl-c">#</span> Example</span>
$ python eval_image_classifier.py \
    --alsologtostderr \
    --checkpoint_path=<span class="pl-smi">${CHECKPOINT_FILE}</span> \
    --dataset_dir=<span class="pl-smi">${DATASET_DIR}</span> \
    --dataset_name=imagenet \
    --dataset_split_name=validation \
    --model_name=inception_v3</pre></div>
<p>See the <a href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim#evaluation-loop">evaluation module example</a> for an example of how to evaluate a model at multiple checkpoints during or after the training.</p>
<h1><a href="#exporting-the-inference-graph" aria-hidden="true" class="anchor" id="user-content-exporting-the-inference-graph"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Exporting the Inference Graph</h1>
<p><a id="user-content-Export"></a></p>
<p>Saves out a GraphDef containing the architecture of the model.</p>
<p>To use it with a model name defined by slim, run:</p>
<div class="highlight highlight-source-shell"><pre>$ python export_inference_graph.py \
  --alsologtostderr \
  --model_name=inception_v3 \
  --output_file=/tmp/inception_v3_inf_graph.pb

$ python export_inference_graph.py \
  --alsologtostderr \
  --model_name=mobilenet_v1 \
  --image_size=224 \
  --output_file=/tmp/mobilenet_v1_224.pb</pre></div>
<h2><a href="#freezing-the-exported-graph" aria-hidden="true" class="anchor" id="user-content-freezing-the-exported-graph"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Freezing the exported Graph</h2>
<p>If you then want to use the resulting model with your own or pretrained
checkpoints as part of a mobile model, you can run freeze_graph to get a graph
def with the variables inlined as constants using:</p>
<div class="highlight highlight-source-shell"><pre>bazel build tensorflow/python/tools:freeze_graph

bazel-bin/tensorflow/python/tools/freeze_graph \
  --input_graph=/tmp/inception_v3_inf_graph.pb \
  --input_checkpoint=/tmp/checkpoints/inception_v3.ckpt \
  --input_binary=true --output_graph=/tmp/frozen_inception_v3.pb \
  --output_node_names=InceptionV3/Predictions/Reshape_1</pre></div>
<p>The output node names will vary depending on the model, but you can inspect and
estimate them using the summarize_graph tool:</p>
<div class="highlight highlight-source-shell"><pre>bazel build tensorflow/tools/graph_transforms:summarize_graph

bazel-bin/tensorflow/tools/graph_transforms/summarize_graph \
  --in_graph=/tmp/inception_v3_inf_graph.pb</pre></div>
<h2><a href="#run-label-image-in-c" aria-hidden="true" class="anchor" id="user-content-run-label-image-in-c"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Run label image in C++</h2>
<p>To run the resulting graph in C++, you can look at the label_image sample code:</p>
<div class="highlight highlight-source-shell"><pre>bazel build tensorflow/examples/label_image:label_image

bazel-bin/tensorflow/examples/label_image/label_image \
  --image=<span class="pl-smi">${HOME}</span>/Pictures/flowers.jpg \
  --input_layer=input \
  --output_layer=InceptionV3/Predictions/Reshape_1 \
  --graph=/tmp/frozen_inception_v3.pb \
  --labels=/tmp/imagenet_slim_labels.txt \
  --input_mean=0 \
  --input_std=255</pre></div>
<h1><a href="#troubleshooting" aria-hidden="true" class="anchor" id="user-content-troubleshooting"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Troubleshooting</h1>
<p><a id="user-content-Troubleshooting"></a></p>
<h4><a href="#the-model-runs-out-of-cpu-memory" aria-hidden="true" class="anchor" id="user-content-the-model-runs-out-of-cpu-memory"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The model runs out of CPU memory.</h4>
<p>See
<a href="https://github.com/tensorflow/models/tree/master/research/inception#the-model-runs-out-of-cpu-memory">Model Runs out of CPU memory</a>.</p>
<h4><a href="#the-model-runs-out-of-gpu-memory" aria-hidden="true" class="anchor" id="user-content-the-model-runs-out-of-gpu-memory"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The model runs out of GPU memory.</h4>
<p>See
<a href="https://github.com/tensorflow/models/tree/master/research/inception#adjusting-memory-demands">Adjusting Memory Demands</a>.</p>
<h4><a href="#the-model-training-results-in-nans" aria-hidden="true" class="anchor" id="user-content-the-model-training-results-in-nans"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The model training results in NaN's.</h4>
<p>See
<a href="https://github.com/tensorflow/models/tree/master/research/inception#the-model-training-results-in-nans">Model Resulting in NaNs</a>.</p>
<h4><a href="#the-resnet-and-vgg-models-have-1000-classes-but-the-imagenet-dataset-has-1001" aria-hidden="true" class="anchor" id="user-content-the-resnet-and-vgg-models-have-1000-classes-but-the-imagenet-dataset-has-1001"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The ResNet and VGG Models have 1000 classes but the ImageNet dataset has 1001</h4>
<p>The ImageNet dataset provided has an empty background class which can be used
to fine-tune the model to other tasks. If you try training or fine-tuning the
VGG or ResNet models using the ImageNet dataset, you might encounter the
following error:</p>
<div class="highlight highlight-source-shell"><pre>InvalidArgumentError: Assign requires shapes of both tensors to match. lhs shape= [1001] rhs shape= [1000]</pre></div>
<p>This is due to the fact that the VGG and ResNet V1 final layers have only 1000
outputs rather than 1001.</p>
<p>To fix this issue, you can set the <code>--labels_offset=1</code> flag. This results in
the ImageNet labels being shifted down by one:</p>
<h4><a href="#i-wish-to-train-a-model-with-a-different-image-size" aria-hidden="true" class="anchor" id="user-content-i-wish-to-train-a-model-with-a-different-image-size"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>I wish to train a model with a different image size.</h4>
<p>The preprocessing functions all take <code>height</code> and <code>width</code> as parameters. You
can change the default values using the following snippet:</p>
<div class="highlight highlight-source-python"><pre>image_preprocessing_fn <span class="pl-k">=</span> preprocessing_factory.get_preprocessing(
    preprocessing_name,
    <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">MY_NEW_HEIGHT</span>,
    <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">MY_NEW_WIDTH</span>,
    <span class="pl-v">is_training</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</pre></div>
<h4><a href="#what-hardware-specification-are-these-hyper-parameters-targeted-for" aria-hidden="true" class="anchor" id="user-content-what-hardware-specification-are-these-hyper-parameters-targeted-for"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>What hardware specification are these hyper-parameters targeted for?</h4>
<p>See
<a href="https://github.com/tensorflow/models/tree/master/research/inception#what-hardware-specification-are-these-hyper-parameters-targeted-for">Hardware Specifications</a>.</p>
</article>
  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2017 <span title="0.13031s from unicorn-2523930239-wr3vg">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-91f98c37fc84eac24836eec2567e9912742094369a04c4eba6e3cd1fa18902d9.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-dce6306350f9163599cb2e0df38e21189604851a11d003388015e66b0f0353ad.js"></script>
    
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-ddeeef758694e4412bcf3b191504d96b4e880050bf8ca5db7d5240f589d52a9d.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

